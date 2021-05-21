from flask import Flask, render_template
app = Flask(__name__)

# testing render temp
@app.route('/hello')
def say_hello():
    """
    says hello :: this is a docstring demo
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

@app.route('/songs')
def show_songs():
    """renders a list of songs from template"""
    songs_showed = [
        'power - kanye',
        'in my feelings - drake',
        'where you was at - future',
        'mesopotamia - MFR',
        'some-drake-song - DRAKE',
        'the soulja boi collection - big draco',
    ]
    return render_template('songs_list.html', songs=songs_showed)

