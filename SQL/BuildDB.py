import sqlite3

db_file = "CRM.db"
sql ="CREATE TABLE users ( id INT, name TEXT, email TEXT)"

def db_update(dbfile_name,sql):
    connection = sqlite3.connect(dbfile_name) # connect to DB
    cursor = connection.cursor()  # Inisilzed
    cursor.execute(sql) # what to do
    connection.commit() # Done


db_update(db_file,sql)




