from flask import Flask, Blueprint, render_template, session, url_for, redirect
from services.article import get_all_articles
from services.home import *
from db import db_connection

home = Blueprint('home', __name__)

@home.route('/')
def index():
    img_url = ''
    if session:
        image_file = ''
        image_file = str(session.get('image_file'))
        img_url = url_for('static', filename='user_profile/' + image_file )
    content = panel()
    articles = get_newest_article(5)
    return render_template('index.html', content=content, img_url=img_url, articles=articles)