from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, URL
from flask_wtf.file import FileField, FileAllowed, FileRequired

import os

from ...settings import ALLOWED_EXTENSIONS


class UploadFromLocal(FlaskForm):
    photo = FileField(
        'Photo',
        validators=[
            FileRequired(),
            FileAllowed(ALLOWED_EXTENSIONS)
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
