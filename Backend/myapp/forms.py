from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, URL
from flask_wtf.file import FileField, FileAllowed, FileRequired
from .models import User
from .config import ALLOWED_EXTENSIONS


class RegisterForm(FlaskForm):
    username = StringField(
        'Username', 
        validators=[
            DataRequired(), 
            # Length(min=4, max=32)
        ]
    )
    email = StringField(
        'Email Address: ', 
        validators=[
            DataRequired(), 
            # Email(message='Enter a valid email.'),
            # Length(min=6)
        ]
    )
    password = PasswordField(
        'Password: ', 
        validators=[
            DataRequired(), 
            # Length(min=6, max=128)
        ]
    )
    confirm = PasswordField(
        'Confirm Password: ', 
        validators=[
            DataRequired(), 
            EqualTo('password', message='Passwords must match.')
        ]
    )
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Please use a different email address.')


class LoginForm(FlaskForm):
    username = StringField(
        'Username: ', 
        validators=[
            DataRequired(), 
        ]
    )
    password = PasswordField(
        'Password: ', 
        validators=[
            DataRequired(), 
        ]
    )
    submit = SubmitField('Login')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data)
        if not user:
            raise ValidationError('Username does not exist.')


class UploadFromLocal(FlaskForm):
    photo = FileField(
        'Photo', 
        validators=[
            FileRequired(), 
            FileAllowed(ALLOWED_EXTENSIONS, 'Images only!')
        ]
    )
    submit = SubmitField('Upload')


class UploadFromURL(FlaskForm):
    photo = StringField(
        'Photo', 
        validators=[
            DataRequired(), 
            URL()
        ]
    )
    submit = SubmitField('Upload')