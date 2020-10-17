import sqlite3

connection = sqlite3.connect('data.db')

createTableUsers = 'CREATE TABLE users (id int, username text, password, text)'
connection.cursor().execute(createTableUsers)
