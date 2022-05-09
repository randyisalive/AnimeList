from db import db_connection


def get_user_by_id(id):
    db = db_connection()
    cur = db.cursor()
    sql = 'SELECT name, email, role_id, password, FirstName, LastName, Region, Country, image_file, roleName FROM users WHERE id = %s' % id
    cur.execute(sql)
    account = cur.fetchone()
    cur.close()
    db.close()
    return account
