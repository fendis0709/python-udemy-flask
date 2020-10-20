import sqlite3


connection = sqlite3.connect('data.db')

# Create table 'users'
createTable = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)'
connection.cursor().execute(createTable)

# Create table 'students'
createTable = 'CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)'
connection.cursor().execute(createTable)

connection.commit()

connection.close()
