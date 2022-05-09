from flask import Flask, request, redirect, render_template, Blueprint, session, url_for
from db import db_connection
from services.forum import *
from services.home import panel

forum = Blueprint('forum', __name__)


@forum.route('/', methods=['GET'])
def index():
    img_url = ''
    if session:
        image_file = ''
        image_file = str(session.get('image_file'))
        img_url = url_for('static', filename='user_profile/' + image_file )
    forums = get_all_forum()
    return render_template('forum/index.html', forums=forums, img_url=img_url)

@forum.route('/read/<id>/<title>', methods=['POST', 'GET'])
def read(id, title):
    img_url = ''
    if session:
        image_file = ''
        image_file = str(session.get('image_file'))
        img_url = url_for('static', filename='user_profile/' + image_file )
    comment = get_comments_by_forum_id(id)
    comments = get_all_comments()
    reply = get_reply_by_comment_id(id)
    return render_template('forum/read.html', id=id, title=title, comment=comment, reply=reply, comments=comments, img_url=img_url)

@forum.route('/comment/<id>/<title>', methods=['POST', 'GET'])
def comment(id, title):
    img_url = ''
    if session:
        image_file = ''
        image_file = str(session.get('image_file'))
        img_url = url_for('static', filename='user_profile/' + image_file )
    user_id = session.get('id')
    username = session.get('name')
    content = panel()
    if request.method == 'POST':
        comment = request.form['comment']
        db = db_connection()
        cur = db.cursor()
        params = (user_id, id, comment, username)
        cur.execute('INSERT INTO comments (user_id, forum_id, body, username) VALUES (%s, %s, %s, %s)', params)
        db.commit()
        cur.close()
        db.close()
        return redirect(url_for('forum.read', title=title, id=id))
    return render_template('forum/add_comment.html', content=content, img_url=img_url)