import pymysql


def db_connection():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        database='anime_blog',
        user='root',
        password=''
    )
    return conn
