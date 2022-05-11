from flask import Flask, Blueprint, render_template, session, url_for, redirect
from services.article import get_all_articles
from services.forum import get_total_forum_by_id
from services.home import *
from db import db_connection

home = Blueprint('home', __name__)

@home.route('/')
def index():
    total_forum = ''
    img_url = ''
    if session:
        id = session.get('id')
        image_file = ''
        image_file = str(session.get('image_file'))
        img_url = url_for('static', filename='user_profile/' + image_file )
        total_forum = get_total_forum_by_id(id)
    content = panel()
    articles = get_newest_article(5)
    return render_template('index.html', content=content, img_url=img_url, articles=articles, total_forum=total_forum)