import sqlite3

db_file = "users.db"

def db_update(dbfile_name,sql):
    connection = sqlite3.connect(dbfile_name) # connect to DB
    cursor = connection.cursor()  # Inisilzed
    cursor.execute(sql) # what to do
    data_table = cursor.fetchall()
    print(data_table)

sql = "SELECT * FROM login WHERE username = 'shalom'-- AND password='dsfdsagfddsg'"
db_update(db_file,sql)

