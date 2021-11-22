from enum import unique
from re import U
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class BioForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    bio = TextAreaField('Bio')
    country = SelectField('Country', validate_choice=False)
    city = StringField('City')
    submit = SubmitField('Change personal info')

class ListForm(FlaskForm):
    header = StringField('Heading',validators=[DataRequired()])
    game = StringField('Game',validators=[DataRequired()])
    platform = StringField('Platform',validators=[DataRequired()])
    info = TextAreaField('Info')
    id = HiddenField()
    submit = SubmitField('Submit a listing')


class FindForm(FlaskForm):
    game = SelectField('Choose game', choices=[('All', 'All')])
    country = SelectField('Choose country', choices=[('All', 'All')])
    city = SelectField('Choose city', choices=[('All', 'All')])
    submit = SubmitField('Search')