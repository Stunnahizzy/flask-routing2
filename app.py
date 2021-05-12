
from flask import Flask, request

app = Flask(__name__)

# return a name backwards
@app.route('/user/<username>')
def say_hello_var(username):
    greet = F'Hi, {username}'
    return greet[::-1]


# return a number squared
@app.route('/num/')
def square(number):
    return str(number * number)

# GET, reqs
# return a name n number of times
@app.route('/numname/<int:num>/<name>')
def numnamer(num,name):
    return str(name * 5)

@app.route('/hello', methods=['GET']) #GET is the default method
def say_hello():
    return "Hello, World!"
    return """
    <body style="background-color='black'">
        <h1>fifth of w</h1>
    </body>
    """
# return a number doubled
@app.route('/double')
def double():
    number = request.args.get('number')
    number = int(number)
    return str(number * 2)
    
# search action route
@app.route('/search')
def search_page():
    name = request.args.get('name')
    category = request.args.get('category')
    num = request.args.get('num')
    return f"You searched for {name} in the category {category}"

# search form route
@app.route('/search_form')
def search_form():
    return """
    <form action='/search'>
        Type in the product name: <input type='text' name='name'>
        <br>
        Type in the category: <input type='text' name='category'>
        <br><br>
        <input type='submit'>
    </form>
    """


# login GET REQ
@app.route('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    return f"username is {username} & password is {password}"


# POST REQ LOGIN FORM
@app.route('/login_form')
def login_form():
    return """
    <form action='/login' method='POST'>
        Username: <input type='text' name='username'>
        <br>
        Password: <input type='password' name='password'> 
        <br>
        <input type='submit'>
    </form>
    """


