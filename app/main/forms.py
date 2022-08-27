from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, FileField, RadioField, DateField, SelectField
from wtforms import validators
from wtforms.validators import Email, EqualTo, ValidationError, DataRequired


class ProfileForm(FlaskForm):
    city = StringField('Место проживания:', validators=[DataRequired()])
    education = StringField('Образование', validators=[DataRequired()])
    mastery = StringField('Специализация', validators=[DataRequired()])
    skill = SelectField('Проф. навыки',choices=["None", "pyhton"])
    birthday = DateField('Datetime', format='%Y-%m-%d', validators=(validators.Optional(),))
    contact = StringField('Контактные данные', description="номер телефона")
    submit = SubmitField('Submit')