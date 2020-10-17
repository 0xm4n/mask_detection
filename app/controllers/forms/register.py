from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            # Email("This field requires a valid email address")
            # Length(min=6)
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
        ]
    )
    confirm = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    role = BooleanField(
        'Administrator permissions'
    )
    submit = SubmitField('Sign up')