import sqlite3


connection = sqlite3.connect('data.db')

createTable = 'CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)'
connection.cursor().execute(createTable)

connection.commit()

connection.close()
