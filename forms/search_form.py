from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField
from wtforms.validators import DataRequired, InputRequired
from .categories import choices


class SearchForm(FlaskForm):
    category = SelectField(u'Categoria', choices=choices, validators=[InputRequired()])
    town = StringField('Ciudad', validators=[DataRequired()])
