from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class BioForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    bio = TextAreaField('Bio')
    country = StringField('Country')
    city = StringField('City')
    submit = SubmitField('Change personal info')

class ListForm(FlaskForm):
    header = StringField('Heading',validators=[DataRequired()])
    game = StringField('Game',validators=[DataRequired()])
    platform = StringField('Platform',validators=[DataRequired()])
    info = TextAreaField('Info')
    id = HiddenField()
    submit = SubmitField('Submit a listing')