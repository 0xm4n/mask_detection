from flask import Blueprint, render_template
from flask import request, flash, redirect, url_for
from flask_login import login_required, logout_user

from ..models import db
from ..models.user import User
from .forms.login import LoginForm
from .forms.recover import SearchAccountForm, ResetPasswordForm

bp = Blueprint('detection', __name__, template_folder='../templates')


@bp.route('/home')
@login_required
def home():
    return render_template('home.html')


@bp.route('/upload_history')
@login_required
def upload_history():
    return render_template('history.html')