from flask import redirect, request, render_template, Blueprint, url_for, session
from db import db_connection
from services.super_user import delete_account_by_id, get_all_user


super_user = Blueprint('super_user', __name__)

@super_user.route('/')
def index():
    role_id = session.get('role_id')
    if not role_id == 1:
        return render_template('admin/401.html')
    accounts = get_all_user()
    return render_template('admin/index.html', accounts=accounts)

@super_user.route('/delete/<id>')
def delete(id):
    id = delete_account_by_id(id)
    return redirect(url_for('super_user.index'))