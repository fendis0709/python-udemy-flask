import sqlite3


class Student:
    def __init__(self, _id: int, name: str):
        self.id = _id
        self.name = name

    # Memformat data kedalam format JSON
    def _json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    # Menampilkan semua data
    @classmethod
    def get(cls):
        connection = sqlite3.connect('data.db')

        query = 'SELECT * FROM students ORDER BY name'
        result = connection.cursor().execute(query)
        rows = result.fetchmany()

        connection.close()

        return rows

    # Menampilkan data berdasarkan id
    @classmethod
    def find(cls, id: int):
        connection = sqlite3.connect('data.db')

        query = 'SELECT * FROM students WHERE id = ?'
        result = connection.cursor().execute(query, (id,))
        result = result.fetchone()

        connection.close()

        if result:
            return cls(*result)

        return None

    # Menambahkan data
    def insert(self):
        connection = sqlite3.connect('data.db')

        query = 'INSERT INTO students VALUES (NULL, ?)'
        connection.cursor().execute(query, (self.name,))

        connection.commit()

        connection.close()

        return None

    # Memperbarui data berdasarkan id
    def update(self, id: int):
        connection = sqlite3.connect('data.db')

        query = 'UPDATE students SET name = ? WHERE id = ?'
        connection.cursor().execute(query, (self.name, id))

        connection.commit()

        connection.close()

        return None

    # Menghapus data berdasarkan id
    @classmethod
    def delete(cls, id: int):
        connection = sqlite3.connect('data.db')

        query = 'DELETE FROM students WHERE id = ?'
        connection.cursor().execute(query, (id,))

        connection.commit()

        connection.close()

        return None
