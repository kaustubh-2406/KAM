from flask import Flask, render_template, request
app = Flask(__name__)

# this is some dummy data for development pourpouse
products=products = [
    {'name': "Potatoes", 'qty': 1, 'unit': "quintel", 'price': 100, 'isVerified': True, 'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt sit nobis ab est voluptatum nisi non numquam earum quis praesentium.'},
    {'name': "Potatoes", 'qty': 1, 'unit': "quintel", 'price': 100, 'isVerified': True, 'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt sit nobis ab est voluptatum nisi non numquam earum quis praesentium.'},
    {'name': "Potatoes", 'qty': 1, 'unit': "quintel", 'price': 100, 'isVerified': True, 'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt sit nobis ab est voluptatum nisi non numquam earum quis praesentium.'},
    {'name': "Potatoes", 'qty': 1, 'unit': "quintel", 'price': 100, 'isVerified': True, 'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt sit nobis ab est voluptatum nisi non numquam earum quis praesentium.'},
    {'name': "Onions", 'qty': 2, 'unit': "quintel", 'price': 200, 'isVerified': False, 'desc': 'Lorem ipsum.Lorem ipsum dolor sit ab est voluptatum nisi amet consectetur adipi dolor sit amet ur adiisicing elit. Nesciunt sit nobis ab est voluptatum nisi non numquam earum quis praesentium.'},
    {'name': "Onions", 'qty': 2, 'unit': "quintel", 'price': 200, 'isVerified': True, 'desc': 'Lorem ipsum.Lorem ipsum dolor sit ab est voluptatum nisi amet consectetur adipi dolor sit amet ur adiisicing elit. Nesciunt sit nobis ab est voluptatum nisi non numquam earum quis praesentium.'}
]

@app.route('/')
def index():
    return render_template('index.html', items=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method== 'GET':
        return render_template('login-page.html')
    else:
        username = request.form['username']
        password = request.form['password']
        print(username, ' -> ', password)
        return f'{username} is logged in'

if __name__ == '__main__':
    app.run(debug=True)
