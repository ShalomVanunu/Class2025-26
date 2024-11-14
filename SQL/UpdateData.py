import sqlite3

db_file = "users.db"

def db_update(dbfile_name,sql):
    connection = sqlite3.connect(dbfile_name) # connect to DB
    cursor = connection.cursor()  # Inisilzed
    cursor.execute(sql) # what to do
    connection.commit() # Done

username_list = ['shalom','liroy','dana','linoy','daria']
password_list = ['Password1','Password2','Password2','3141','123']

for index in range(5):
    sql =f"INSERT INTO login VALUES ('{username_list[index]}','{password_list[index]}') "
    db_update(db_file,sql)