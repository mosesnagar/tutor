from tutor import db


class Model(db.Model):
    __tablename__ = 'models'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name
        }