from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class SearchAccountForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
        ]
    )
    search = SubmitField('Search')
