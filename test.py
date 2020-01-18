import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users(id int,username text, password text)"
cursor.execute(create_table)

user = (1, 'hello', 'world')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user)
connection.commit()
connection.close()