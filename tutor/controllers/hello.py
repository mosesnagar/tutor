from flask import render_template
from .. import app

 
def hello():
    return render_template('index.html')
