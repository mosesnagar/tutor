from .. import app
from ..controllers import home, register, login, forms


@app.route('/')
@app.route("/home")
def index_route():
    return home.home()


@app.route("/register", methods=[ 'GET', 'POST']) 
def register_route():
    return register.register()

@app.route("/login", methods=['GET', 'POST'])
def login_route():
    return login.login()