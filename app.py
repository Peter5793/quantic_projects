from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/shop', methods=['GET'])
def shop():
    types = ['12oz Medium Roast', '24oz French Roast', '96oz Whole Beans']
    return render_template('shop.html', types=types)

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')