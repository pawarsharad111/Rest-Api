
import sqlite3



connection=sqlite3.connect('data.db')
cursor=connection.cursor()

CREATE_QUERY="CREATE TABLE  IF NOT EXISTS user(id TEXT, password TEXT)"
cursor.execute(CREATE_QUERY)

connection.commit()
connection.close()