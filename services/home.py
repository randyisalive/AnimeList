from flask import Flask
from flask import session
from db import db_connection

def panel():
    content = {'panel1':'MyAnimeList',
               'panel2':'Login',
               'panel3':'Signup',
               'panel4':'Featured Article',
               'panel5':'My Article',
               'panel6':'Edit Article',
               'panel7':'Post Comment',
               'panel8':'Profile'}
    return content

def get_img_file(id):
    id = session.get('id')
    db = db_connection()
    cur = db.cursor()
    sql = 'SELECT image_file FROM users WHERE id = %s' % id
    cur.execute(sql)
    img_file = cur.fetchone()
    image = img_file[0]
    cur.close()
    db.close()
    return image, id


def get_newest_article(size):
    db = db_connection()
    cur = db.cursor()
    sql = 'SELECT title, body FROM articles ORDER BY id DESC'
    cur.execute(sql)
    articles = cur.fetchmany(size)
    cur.close()
    db.close()
    return articles