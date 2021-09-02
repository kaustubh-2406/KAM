from flask import render_template, url_for
from package import app, products
from package.models import Farmer, Crop, Trader

@app.route('/')
def index():
    items = Crop.query.all()
    items.extend(products) # this is just for development pourpose
    return render_template('index.html', items=items)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method== 'GET':
        return render_template('login-page.html')
    else:
        username = request.form['username']
        password = request.form['password']
        print(username, ' -> ', password)
        return f'{username} is logged in'
