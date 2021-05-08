
from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search_page():
    name = request.args.get('name')
    category = request.args.get('category')
    return f"You searched for {name} in the category {category}"

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

@app.route('/hello')
def say_hello():
    return "Hello, World!"

# return a name backwards
@app.route('/user/<username>')
def say_hello_var(username):
    greet = F'Hi, {username}'
    return greet[::-1]

# return a number doubled
@app.route('/double/<int:the_number>')
def double(the_number):
    return str(the_number * 2)

# return a number squared
@app.route('/num/<int:number>')
def square(number):
    return str(number * number)

# return a name n number of times
@app.route('/numname/<int:num>/<name>')
def numnamer(num,name):
    return str(name * 5)

@app.route('/main')
def mainer():   
    return """
    <body style="background-color='black'">
        <h1>fifth of w</h1>
    </body>
    """