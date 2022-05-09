from flask import Flask, request, redirect, render_template, flash, Blueprint, session, url_for
from db import db_connection
from services.article import get_all_articles, get_article_by_id, get_article_by_title
from services.home import panel


article = Blueprint('article', __name__)

@article.route('/', methods=['POST','GET'])
def index():  
    img_url = ''
    if session:
        image_file = ''
        image_file = str(session.get('image_file'))
        img_url = url_for('static', filename='user_profile/' + image_file )
    content = panel()
    article = get_all_articles()
    return render_template('article/index.html', article=article, content=content, img_url=img_url)

@article.route('/<id>/<title>')
def read_article(id, title):
    content = panel()
    article = get_article_by_id(id)
    return render_template('article/read_article.html', id=id, title=title, article=article, content=content)

@article.route('/create', methods=['POST', 'GET'])
def create():
    content = panel()
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        user_id = session.get('id')
        db = db_connection()
        cur = db.cursor()
        params = (title, body, user_id)
        cur.execute('INSERT INTO articles (title, body, user_id) VALUES ( %s, %s, %s)', params)
        db.commit()
        cur.close()
        db.close()
        return redirect(url_for('article.index'))
    return render_template('article/create.html', content=content)

@article.route('/edit/<id>/<title>', methods=['POST', 'GET'])
def edit(id, title):
    id = id
    title = title
    img_url = ''
    if session:
        image_file = ''
        image_file = str(session.get('image_file'))
        img_url = url_for('static', filename='user_profile/' + image_file )
    if request.method == 'POST':
        id = id
        title = title
        conn = db_connection()
        cur = conn.cursor()
        title = request.form['title']
        body = request.form['body']
        brief = request.form['brief']
        user_id = session.get('id')
        title = title.strip()
        body = body.strip()
        brief = brief.strip()
        sql_params = (title, body, brief, user_id, id)
        sql = "UPDATE articles SET title = '%s', body = '%s', brief = '%s', user_id = '%s' WHERE id = %s" % sql_params
        print(sql)
        cur.execute(sql)
        cur.close()
        conn.commit()
        conn.close()
        # use redirect to go to certain url. url_for function accepts the
        # function name of the URL which is function index() in this case
        return redirect(url_for('article.index'))
    db = db_connection()
    cur = db.cursor()
    sql = 'SELECT id,title,body,brief,user_id FROM articles WHERE id = %s' % id
    cur.execute(sql)
    article = cur.fetchone()
    cur.close()
    db.close()
    content = panel()
    return render_template('article/edit.html', img_url=img_url, content=content, title=title, article=article, id=id,)
    