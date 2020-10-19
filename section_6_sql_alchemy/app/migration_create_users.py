import sqlite3


connection = sqlite3.connect('data.db')

createTable = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)'
connection.cursor().execute(createTable)

connection.commit()

connection.close()
