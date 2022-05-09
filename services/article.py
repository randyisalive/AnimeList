from db import db_connection


def get_all_articles():
    db = db_connection()
    cur = db.cursor()
    sql = 'SELECT * FROM articles ORDER BY id'
    cur.execute(sql)
    article = cur.fetchall()
    cur.close()
    db.close()
    return article


def get_article_by_id(id):
    db = db_connection()
    cur = db.cursor()
    sql = 'SELECT body FROM articles WHERE id = %s' % id
    cur.execute(sql)
    article = cur.fetchone()
    cur.close()
    db.close()
    return article

def get_article_by_title(q):
    db = db_connection()
    cur = db.cursor()
    sql = 'SELECT * FROM articles WHERE MATCH (title) AGAINST ( %s IN NATURAL LANGUAGE MODE);' % q
    cur.execute(sql)
    filtered = cur.fetchall()
    cur.close()
    db.close()
    return filtered