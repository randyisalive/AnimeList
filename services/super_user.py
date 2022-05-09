from django.shortcuts import redirect
from db import db_connection



def get_all_user():
    db = db_connection()
    cur = db.cursor()
    sql = 'SELECT id, name, email, role_id, password, FirstName, LastName, Region, Country, image_file FROM users ORDER BY id'
    cur.execute(sql)
    account = cur.fetchall()
    cur.close()
    db.close()
    return account

def delete_account_by_id(id):
    db = db_connection()
    cur = db.cursor()
    sql = 'DELETE FROM users WHERE id = %s' % id
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()
