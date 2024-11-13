import sqlite3

db_file = "CRM.db"

def db_update(dbfile_name,sql):
    connection = sqlite3.connect(dbfile_name) # connect to DB
    cursor = connection.cursor()  # Inisilzed
    cursor.execute(sql) # what to do
    connection.commit() # Done

# # insert new data to DB file
# sql ="INSERT INTO users VALUES (1,'moshe', 'moshe@gmail.com')"
# db_update(db_file,sql)
# upadte data to DB file
sql ="UPDATE users SET id=2 WHERE name='moshe'"
db_update(db_file,sql)