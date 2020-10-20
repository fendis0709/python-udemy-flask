import sqlite3
from database import db


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

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
        return Student.query.order_by(cls.name).all()

    # Menampilkan data berdasarkan id
    @classmethod
    def find(cls, id: int):
        return cls.query.filter_by(id=id).first()

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

    # Menyimpan data (Insert & Update)
    def save(self):
        db.session.add(self)
        db.session.commit()

        return None

    # Menghapus data berdasarkan id
    @classmethod
    def delete(cls, id: int):
        cls.query.filter_by(id=id).delete()
        db.session.commit()

        return None
