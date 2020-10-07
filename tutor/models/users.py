from .. import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

    def hash_pass(plaintext):
        return bcrypt.generate_password_hash(plaintext).decode('utf-8')

    def __repr__(self):
        return "'id': {0}, 'username': {1}, 'email': {2}".format(self.id, self.username, self.email)
