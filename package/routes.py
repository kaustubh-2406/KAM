from flask import render_template, url_for, request, jsonify, redirect, session
from package import app, products, db, bcrypt
from package.models import Farmer, Crop, Trader

@app.route('/')
def index():
    items = Crop.query.all()
    items.extend(products) # this is just for development pourpose
    return render_template('index.html', items=items)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method== 'GET':
        return render_template('signup.html')
    else:
        try:
            username = request.form['username']
            password = request.form['password']
            print(username, password)
            user = Farmer(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            session.expire_on_commit=False
            return redirect(url_for('login'), code=302)
        except:
            return redirect(url_for('404'), code=302)

@app.route('/dashboard')
def dashboard():
    if not session.get('user'):
        return redirect('/login')
    else:
        user = session['user']
        return render_template('dashboard.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login-page.html')
    else:
        # it is post request
        try:
            username = request.form['username']
            password = request.form['password']
            user = {}
            farmers = Farmer.query.filter_by(username=username).all()

            for farmer in farmers:
                if bcrypt.check_password_hash(farmer.hash_password, password):
                    user = farmer
                    session['user'] = user
                    break;
                else:
                    return render_template('404.html')
            
            return redirect('/dashboard', code=302)
        except:
            return 'Something went wrong'

@app.route('/404')
def not_found():
    return render_template('404.html')

@app.route('/add-crop', methods=["POST"])
def add_crop():
    user = session['user']
    print('============', request)
    crop = Crop(
        name = request.args['crop'],
        qty = request.args['quantity'],
        price = request.args['price'],
        desc = request.args['desc']
    )
    db.session.add(crop)
    db.session.commit()

    crop.owner = user.id
    db.session.add(crop)
    db.session.commit()

    return redirect('/dashboard', code=302)