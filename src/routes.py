from src import src
from flask import render_template

@src.route('/')
@src.route('/index')
def index():
    return render_template('index.html')