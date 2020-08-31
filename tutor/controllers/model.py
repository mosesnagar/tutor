from ..models import Model
from .. import db
from flask import jsonify


def getAllModels():
        models = Model.query.all()
        return jsonify([e.serialize() for e in models])


def createNewModel(modelName):
    model = Model(name=modelName)
    db.session.add(model)
    db.session.commit()
    return jsonify({'id' : model.id, 'status' : 200})
    