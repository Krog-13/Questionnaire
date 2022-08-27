from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, FieldList, RadioField, DateField, SelectField
from wtforms import validators
from wtforms.validators import EqualTo, ValidationError, DataRequired, Length, \
    regexp
import re
import datetime

class ProfileForm(FlaskForm):
    label = [('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text'),
            ('jv', 'Java'), ('ph', 'PHP'), ('ex', 'Excel'),
             ]
    city = StringField('Место проживания:', validators=[DataRequired(),
                                                        Length(min=2)])
    education = StringField('Образование', validators=[DataRequired()])
    mastery = StringField('Специализация', validators=[DataRequired()])
    skill = SelectField("Проф. навык", choices=label)




    def detect_age(self, age):
        res = datetime.datetime.today().year - self.birthday.data.year
        if res < 18:
            raise ValidationError("Ваш возраст меньше 18")

    birthday = DateField('Datetime', format='%Y-%m-%d', validators=(validators.Optional(),
                                                                    detect_age))
    def validate_number_phone(self, number):
        if not re.search('^\+7\d{10}$', self.contact.data):
            raise ValidationError("Вы ввели не корректный номер")

    contact = StringField('Контактные данные', description="номер телефона",
                          validators=[validate_number_phone])
    submit = SubmitField('Submit')