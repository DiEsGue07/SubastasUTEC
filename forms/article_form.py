from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileField, FileRequired
from .categories import choices
from wtforms.fields import (StringField,
                            SelectField,
                            IntegerField,
                            TimeField,
                            TextAreaField)


class ArticleForm(FlaskForm):
    name = StringField('Nombre del articulo', validators=[DataRequired()])
    category = SelectField(u'Categoria', choices=choices)
    town = StringField('Ciudad', validators=[DataRequired()])
    minimal_price = IntegerField('Precio minimo')
    article_image = FileField('Imagen de articulo', validators=[FileRequired()])
    end_day = StringField('Fecha final', validators=[InputRequired()])
    end_time = TimeField('Hora final', validators=[InputRequired()])
    description = TextAreaField('Descripcion', validators=[DataRequired()])
