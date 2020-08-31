from .. import app
from ..controllers import model

# example to get all models
@app.route('/models')
def models_route():
    return model.getAllModels()


# example of a route with different methods
# example to return a json 
@app.route('/model/store', methods=['GET', 'POST'])
def store_book_route():
    return model.createNewModel(modelName='model')