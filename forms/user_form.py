from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    email = StringField('Login/Email', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    s_name = StringField('Фамилия', validators=[DataRequired()])
    f_name = StringField('Имя', validators=[DataRequired()])
    salary = IntegerField('Оплата за час', validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться')


class UpdateUserForm(FlaskForm):
    email = StringField('Login/Email')
    s_name = StringField('Фамилия')
    f_name = StringField('Имя')
    country = StringField("Страна")
    sex = SelectField("Пол", choices=['man', 'women'])
    vk = StringField("Ссылка на вк")
    git = StringField("Ссылка на GitHub")

    submit = SubmitField('Сохранить')