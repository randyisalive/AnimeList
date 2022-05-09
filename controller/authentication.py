from flask import (
    Blueprint, flash, render_template, request, session, url_for,redirect
    )
from matplotlib.style import use
from services.authentication import *
from controller.home import *
from db import db_connection



auth = Blueprint('auth', __name__)





@auth.route('/login', methods=['POST', 'GET'])
def login():
    error = ''
    content = panel()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = db_connection()
        cur = conn.cursor()
        params = (username,password)
        sql = "SELECT id, name, password, email, FirstName, LastName, Region, Country, role_id, image_file FROM users WHERE name = '%s' AND password = '%s' " % params
        cur.execute(sql)
        user = cur.fetchone()
        if user is None:
            error = 'Wrong username or Password'
        else:
            session.clear()
            session['id'] = user[0]
            session['password'] = user[2]
            session['name'] = user[1]
            session['email'] = user[3]
            session['FirstName'] = user[4]
            session['LastName'] = user[5]
            session['Region'] = user[6]
            session['Country'] = user[7]
            session['role_id'] = user[8]
            session['image_file'] = user[9]
            name = session.get('name')
            return redirect(url_for('home.index', name=name ))
        flash(error)
        cur.close()
        conn.close()
    return render_template('login.html', content=content, error=error)

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.index'))

@auth.route('/signup', methods=['POST','GET'])
def signup():
    error = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        role = 'User'
        params = (username,password,email)
        db = db_connection()
        cur = db.cursor()
        cur.execute('SELECT * FROM users WHERE name = %s', (username))
        user = cur.fetchone()
        if user:
            error = 'Account already exist'
        else:
            params = (username,password,email, role)
            cur.execute('INSERT INTO users (name, password, email, role_id, roleName) VALUES (%s, %s, %s, 2, %s)', params)
            db.commit()
            error = 'Account registered!!'
            flash(error)
            cur.close()
            db.close()
        return redirect(url_for('auth.login'))
    return render_template('signup.html', error=error)

@auth.route('/edit/<name>', methods=['POST', 'GET'])
def edit_profile(name):
    name = session.get('name')
    password = session.get('passwrod')
    id = session.get('id')
    image_file = session.get('image_file')
    img_url = url_for('static', filename='user_profile/' + image_file )
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        region = request.form['region']
        country = request.form['country']
        file = request.form['file']
        db = db_connection()
        cur = db.cursor()
        params = (username,password,firstname,lastname,email,region,country,file,id)
        cur.execute('UPDATE users SET name = %s, password = %s, FirstName = %s, LastName = %s, email = %s, Region = %s, Country = %s, image_file = %s WHERE id = %s', params)
        db.commit()
        msg = 'ACCOUNT UPDATED'
        flash(msg)
        session.clear()
        cur.close()
        db.close()
        return redirect(url_for('home.index', name=name, password=password, msg=msg, file=file))
    return render_template('profile/edit.html', name=name, img_url=img_url)

@auth.route('/edit/updated')
def updated():
    return render_template('profile/relogin.html')



@auth.route('/view/<id>/<username>')
def view(id,username):
    content = panel()
    account = get_user_by_id(id)
    return render_template('profile/view.html', account=account, id=id, username=username, content=content)
    