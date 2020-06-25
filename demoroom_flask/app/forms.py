from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class RequestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    demo_name = StringField('Demo Name', validators=[DataRequired()])
    comments = TextAreaField('Additional Comments')
    submit = SubmitField('Request Demo')
