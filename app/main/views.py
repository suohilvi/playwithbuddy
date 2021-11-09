from flask import render_template
from flask_login.utils import login_required
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/find')
def find():
    return render_template('find.html')

@main.route('/user')
@login_required
def user():
    return render_template('user.html')

@main.route('/admin')
@login_required
def admin():
    return render_template('admin.html')
