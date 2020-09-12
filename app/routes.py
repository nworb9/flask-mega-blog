from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Emma'}
    posts = [
        {
            'author': {'username': 'Luke'},
            'body': 'Beautiful day in Flatbush!'
        },
        {
            'author': {'username': 'May'},
            'body': 'Beautiful day in Paris!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
