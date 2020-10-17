import sqlite3

connection = sqlite3.connect('./data.db')

createTableUsers = 'CREATE TABLE users (id int, username text, password text)'
connection.cursor().execute(createTableUsers)

userData = (1, "joko", "12345")
insertUser = 'INSERT INTO users VALUES (?, ?, ?)'
connection.cursor().execute(insertUser, userData)

getUsers = 'SELECT * FROM users'
for user in connection.cursor().execute(getUsers):
    print(user)

connection.commit()

connection.close()
