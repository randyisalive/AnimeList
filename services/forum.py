from db import db_connection


def get_all_forum():
    size = 5
    db = db_connection()
    cur = db.cursor()
    sql = 'SELECT username, users_id, id, title FROM forum'
    cur.execute(sql)
    forums = cur.fetchmany(size)
    cur.close()
    db.close()
    return forums


def get_forum_by_id(id):
    db = db_connection()
    cur = db.cursor()
    params = (id)
    sql = 'SELECT id, title, users_id FROM forum WHERE id = %s' % params
    cur.execute(sql)
    forum = cur.fetchone()
    cur.close()
    db.close()
    return id, forum

def get_all_comments():
    db = db_connection()
    cur = db.cursor()
    sql = 'SELECT * FROM comments ORDER BY id DESC'
    cur.execute(sql)
    comments = cur.fetchall()
    cur.close()
    db.close()
    return comments



def get_comments_by_forum_id(id):
    db = db_connection()
    cur = db.cursor()
    sql = """SELECT c.body, c.forum_id, c.id, c.user_id, f.title, c.username, c.posted_at
             FROM comments c
             LEFT JOIN forum f
             ON c.forum_id = f.id
             WHERE f.id = %s """ % id
    cur.execute(sql)
    comment = cur.fetchone()
    cur.close()
    db.close()
    return comment

def get_reply_by_comment_id(id):
    db = db_connection()
    cur = db.cursor()
    sql = """SELECT c.body, c.forum_id, c.id, c.user_id, r.body, c.username
             FROM reply r
             LEFT JOIN comments c
             ON r.comment_id = c.id
             WHERE c.id = %s """ % id
    cur.execute(sql)
    reply = cur.fetchone()
    cur.close()
    db.close()
    return reply


def post_comment():
    pass