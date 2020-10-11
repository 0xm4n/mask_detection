from flask import Blueprint, render_template
from flask import request, flash, redirect, url_for
from flask_login import login_required, logout_user

from ..models import db
from ..models.user import User
from .forms.login import LoginForm
from .forms.recover import SearchAccountForm

bp = Blueprint('oauth', __name__, template_folder='../templates')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash(u'The username and/or password you specified are not correct.', category='error')
        elif not user.check_password(form.password.data):
            flash(u'The username and/or password you specified are not correct.', category='error')
        else:
            if 'next' in request.values:
                return redirect(request.values['next'])
            return redirect(url_for('detection.home'))
    return render_template('login.html', form=form)


@bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('oauth.login'))


@bp.route('/forgot-password', methods=['GET', 'POST'])
def forget_password():
    form = SearchAccountForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash(u'No Search Results', category='error')
        flash(u'111', category='error')
    return render_template('recover.html', form=form)


@bp.route('/reset-password')
def reset_password():
    return 'success'


@bp.route('/sign-up')
@login_required
def sign_up():
    return 'success'
