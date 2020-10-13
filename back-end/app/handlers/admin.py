from flask import Blueprint, render_template
from flask import request, flash, redirect, url_for
from flask_login import login_required, logout_user

from ..models import db
from ..models.user import User
from .forms.login import LoginForm
from .forms.recover import SearchAccountForm, ResetPasswordForm

bp = Blueprint('admin', __name__, template_folder='../templates')


@bp.route('/add_account')
def add_account():
    return render_template('management.html')