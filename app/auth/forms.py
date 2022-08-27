from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, FileField, RadioField, DateField
from wtforms.validators import Email, EqualTo, DataRequired


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Авторизоваться')


class RegisterForm(FlaskForm):
    fullname = StringField('ФИО', validators=[DataRequired()])
    email = StringField("Почта", validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Зарегистрироватся')


class LoadForm(FlaskForm):
    submit = SubmitField('Submit')