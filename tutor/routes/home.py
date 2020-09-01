from .. import app
from ..controllers import home


@app.route('/')
def index_route():
    return home.home()
