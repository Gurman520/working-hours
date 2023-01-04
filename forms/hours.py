from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, FloatField, SelectMultipleField
from wtforms.validators import DataRequired


class NewHours(FlaskForm):
    create_data = DateField('День когда работали', validators=[DataRequired()])
    hours = FloatField('Количетсво часов', validators=[DataRequired()])
    where = SelectMultipleField("Тип заказчика", choices=["ИП", "Физическое лицо", "ГПХ"],
                               validators=[DataRequired()])
    description = StringField("Описание работы за день")
    submit = SubmitField('Записать')