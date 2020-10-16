from uuid import uuid4

from flask import Blueprint, render_template
from flask import flash, redirect, url_for, request
from flask import jsonify
from werkzeug.security import generate_password_hash

from app import db
from ..models.user import User
from sqlalchemy.sql import exists
from .forms.api_form import RegisterForm

bp = Blueprint('api', __name__, template_folder='../templates/api')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        is_exist = db.session.query(exists().where(User.username == username)).scalar()
        if is_exist:
            success = False
            code = 400
            message = "That username is taken. Try another."
        else:
            password = generate_password_hash(password)
            user = User(str(uuid4()), username, "", password, 1, 1)
            db.session.add(user)
            db.session.commit()
            success = True
            code = 200
            message = "Success"
        res = jsonify(
            success=success,
            error={
                "code": code,
                "message": message
            }
        )
        return res
