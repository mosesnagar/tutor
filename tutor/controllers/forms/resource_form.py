from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL


class ResourceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    link = TextAreaField('Link', validators=[DataRequired(), URL(
        require_tld=True, message="Not a valid URL")])
    submit = SubmitField('Post')
