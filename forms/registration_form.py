from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField


class RegisterForm(FlaskForm):
    full_name = StringField('Nombre Completo', validators=[DataRequired()])
    email = EmailField('Direccion email', validators=[DataRequired(), Email()])
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    adress = StringField('Direccion', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])

