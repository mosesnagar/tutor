from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class AddCourse(FlaskForm):
    name = StringField('Course Name', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Add Course')
