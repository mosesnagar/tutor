from .. import app
from ..controllers import hello


@app.route('/')
def hello_route():
    return hello.hello()
