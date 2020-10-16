from flask import Blueprint, render_template
from flask import request, flash, redirect, url_for
from flask_login import login_required, logout_user, login_user, current_user
from flask_mail import Message

from app import db
from ..models.user import User
from .forms.login import LoginForm
from .forms.recover import SearchAccountForm, ResetPasswordForm, ChangePasswordForm
from ..utils.mail import mail

bp = Blueprint('oauth', __name__, template_folder='../templates')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash(u'The username you specified are not correct.', category='error')
        elif not user.check_password(form.password.data):
            flash(u'The password you specified are not correct.', category='error')
        else:
            login_user(user)
            if 'next' in request.values:
                return redirect(request.values['next'])
            else:
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
            flash(u'No search result, please try again with other username.', category='error')
        elif user.email is '':
            flash(u"This account didn't specified an email. Recover pwd is only for the account setting up by admin "
                  u"which has a specified email ( not for account set up via register API)", category='error')
        else:
            token = user.get_reset_password_token()
            print(user.email)
            print(token)
            msg = Message("Reset Password",
                          sender="ece1779@hotmail.com",
                          recipients=[user.email])
            msg.body = render_template('email/reset_email.txt', user=user, token=token)
            msg.html = render_template('email/reset_email.html', user=user, token=token)
            mail.send(msg)
            flash('Check your email to reset your password.')
            return redirect(url_for('oauth.login'))
    return render_template('reset_request.html', form=form)


@bp.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.verify_reset_password_token(token)

    if not user:
        return redirect(url_for('oauth.login'))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        if form.new_password.data != form.confirm.data:
            flash(u'Passwords must match')
        else:
            user.update_password(form.new_password.data)
            db.session.commit()
            flash('Your Password has been reset.')
            return redirect(url_for('oauth.login'))

    return render_template('reset.html', form=form, token=token)


@bp.route('/settings', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if form.new_password.data != form.confirm.data:
            flash(u'Passwords must match')
        else:
            user = User.query.filter_by(username=current_user.username).first()
            if not user.check_password(form.old_password.data):
                flash(u'Password is not correct')
            else:
                user.update_password(form.new_password.data)
                db.session.commit()
                flash('Your Password has been reset.')
                return redirect(url_for('oauth.login'))
    return render_template('settings.html', form=form)
