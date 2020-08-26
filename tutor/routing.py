from flask import jsonify
from tutor import app, db
from tutor.controllers import hello
from tutor.models import Model


#hello world
@app.route('/')
def hello_route():
    return hello.hello()


# example to get all models
@app.route('/models')
def models_route():
    books = Model.query.all()
    return jsonify([e.serialize() for e in books])


# example of a route with different methods
# example to return a json 
@app.route('/model/store', methods=['GET', 'POST'])
def store_book_route():
    model = Model(name="moshe")
    db.session.add(model)
    db.session.commit()
    return jsonify({'id' : model.id, 'status' : 200})
