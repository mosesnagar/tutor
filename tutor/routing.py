from run import app
from tutor.routes import home

@app.route('/')
def index_route():
    return home.home()