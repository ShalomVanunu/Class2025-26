import sqlite3

db_file = "users.db"
sql ="CREATE TABLE login ( username TEXT, password TEXT)"

def db_update(dbfile_name,sql):
    connection = sqlite3.connect(dbfile_name) # connect to DB
    cursor = connection.cursor()  # Inisilzed
    cursor.execute(sql) # what to do
    connection.commit() # Done


db_update(db_file,sql)


