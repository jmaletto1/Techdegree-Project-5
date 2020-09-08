from flask_wtf import Form
from wtforms import DateField, IntegerField, StringField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length, ValidationError

import models


def title_exists():
    if Journal.select().where(Journal.title == field.data).exists():
        raise ValidationError(
            "It seems a journal with that title already exists.")


class NewEntry(Form):
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Please enter your date as YYYY-MM-DD',
                     validators=[InputRequired(message="Please enter a date.")])
    time_spent = IntegerField('How many hours did you spend on this??',
                              validators=[DataRequired()])
    learnt = TextAreaField('What did you learn?', validators=[DataRequired()])
    resources = TextAreaField(
        'Which resources would you like to list?', validators=[DataRequired()])
