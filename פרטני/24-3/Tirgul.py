# Thread
# DB
# OS

import threading
import os
import sqlite3

# נכתוב תוכנית שמריצה 3 פקודות במקביל ושומר את התוצאות ב-DB

DB_FILE = "data.db"
cmds = ['ping 127.0.0.1', 'whoami', 'ipconfig']

def create_db(dbfile_name,sql):
    connection = sqlite3.connect(dbfile_name) # connect to DB
    cursor = connection.cursor()  # Inisilzed
    cursor.execute(sql) # what to do
    connection.commit() # Done

def run_cmd(command):
    result = os.popen(command).read()
    SQL_INSERT = f"INSERT INTO command VALUES ('{command}','{result}')"
    create_db(DB_FILE, SQL_INSERT)

SQL_CREATE ="""CREATE TABLE IF NOT EXISTS command(
   command text,
   result text);"""

# create Table DB
create_db(DB_FILE,SQL_CREATE)

for cmd in cmds:
    th = threading.Thread(target=run_cmd, args=(cmd,))
    th.start()





