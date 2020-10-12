from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, InputRequired


class SearchAccountForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
        ]
    )
    search = SubmitField('Search')


class ResetPasswordForm(FlaskForm):
    old_password = PasswordField(
        'Old Password',
        validators=[
            DataRequired(),
        ]
    )
    new_password = PasswordField(
        'New Password',
        validators=[
            DataRequired()
        ]
    )
    confirm = PasswordField(
        'Confirm New Password',
        validators=[
            DataRequired(),
            EqualTo('new_password', message='Passwords must match')
        ]
    )
    submit = SubmitField('Change password')
