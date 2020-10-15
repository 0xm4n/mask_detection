from uuid import uuid4

from flask import Blueprint, render_template
from flask import flash, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash

from .forms.register import RegisterForm
from app import db
from ..models.user import User
from sqlalchemy.sql import exists


bp = Blueprint('admin', __name__, template_folder='../templates')


@bp.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():
    if current_user.role == 0:
        flash("you don't have permission to access this page.")
        return redirect(url_for('oauth.login'))
    else:
        form = RegisterForm()
        users = User.query.with_entities(User.username, User.email, User.role)
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = generate_password_hash(form.password.data)
            role = form.role.data
            is_exist = db.session.query(exists().where(User.username == username)).scalar()
            if is_exist:
                print(is_exist)
                flash(u'That username is taken. Try another.')
            elif form.password.data != form.confirm.data:
                flash(u'Passwords must match')
            else:
                user = User(str(uuid4()), username, email, password, role, 1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('admin.add_user'))
    return render_template('management.html', form=form, users=users)



