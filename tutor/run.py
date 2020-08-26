from tutor import app, db
from tutor.models import *

# create all table on DB
db.create_all()


# import routes
from tutor.routing import *


if __name__ == "__main__":
    app.run(debug=True)
