import sqlite3
connection=sqlite3.connect('data.db')
cursor = connection.cursor()

query="CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
select="select * from users"
cursor.execute(query)
cursor.execute(select)
connection.close()