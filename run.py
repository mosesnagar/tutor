from tutor import app, db
from tutor.models import Model


# create all table on DB
db.create_all()


# import routes
from tutor.routes import hello, model


if __name__ == "__main__":
    app.run(debug=True)
