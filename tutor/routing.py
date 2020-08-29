from tutor import app
from tutor.controllers import hello, model


#hello world
@app.route('/')
def hello_route():
    return hello.hello()


# example to get all models
@app.route('/models')
def models_route():
    return model.ModelController.getAllModels()


# example of a route with different methods
# example to return a json 
@app.route('/model/store', methods=['GET', 'POST'])
def store_book_route():
    return model.ModelController.createNewModel(modelName='model')

