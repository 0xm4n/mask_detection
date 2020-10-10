from flask import Blueprint, render_template

bp = Blueprint('oauth', __name__, template_folder='../templates')


@bp.route('/test231')
def hello_world():
    return render_template('index.html')


@bp.route('/test11')
def hello_world11():
    return 'Hello, World123!'
