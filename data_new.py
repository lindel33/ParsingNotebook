# Запись в таблицы БД
# name, number_series, text
import MySQLdb
from settings import login_db, pass_db

connect = MySQLdb.connect('localhost', login_db, pass_db, 'repair_site')
cursor = connect.cursor()


def add_new_model(data):
    sql = ("INSERT INTO repair_home_infotmp (name, number_series, text)"
           " VALUES (%(name)s, %(number_series)s, %(text)s)")
    cursor.execute(sql, data)
    connect.commit()
