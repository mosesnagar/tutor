from tutor import app, db
from tutor.models import *

db.create_all()

from tutor.routing import *

if __name__ == "__main__":
    app.run(debug=True)
