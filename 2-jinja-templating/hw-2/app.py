from flask import Flask, render_template
app = Flask(__name__)

# testing render temp
@app.route('/hello')
def say_hello():
    """
    says hello
    """
    return render_template('greeting.html')

@app.route('/items')
def show_items():
    """ shows a list of items """
    items_to_show = [
        'Pumpkins',
        'Karaoke Machine',
        'Disco Ball'
    ]
    return render_template('items_list.html', items=items_to_show)