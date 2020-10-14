from uuid import uuid4

from flask import Blueprint, render_template
from flask import flash, redirect, url_for
from flask_login import login_required
from werkzeug.security import generate_password_hash

from .forms.register import RegisterForm
from ..models import db
from ..models.user import User


bp = Blueprint('admin', __name__, template_folder='../templates')


@bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = RegisterForm()
    users = User.query.with_entities(User.username, User.email, User.role)
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        role = form.role.data

        user = User(str(uuid4()), username, email, password, role, 1)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('admin.add_user'))
    return render_template('management.html', form=form, users=users)
