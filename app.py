from flask import Flask, render_template, request

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

@app.route('/register', methods=['GET','POST'])
def register():
    message = ""
    error = []
    if request.method == 'POST':
        # Handle registration logic here
        username = request.form['uname']
        password = request.form['pword']
        confirm = request.form['confirm']
        if not username:
            error.append("Username is required.")
        if not password:
            error.append("Password is required.")
        if not confirm:
            error.append("Password confirmation is required.")
        if len(username) < 3:
            error.append("Username must be at least 3 characters long.")
        if password != confirm:
            error.append("Passwords do not match.")
        
        if error:
            message = "Registration failed"
        else:
            message = f"Successfully registered {username}"
    return render_template('register.html', message=message, error= error)