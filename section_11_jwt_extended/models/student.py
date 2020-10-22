from database import db


class StudentModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))
    school = db.relationship('SchoolModel')

    def __init__(self, _id: int, name: str, school_id: int = None):
        self.id = _id
        self.name = name
        self.school_id = school_id

    # Memformat data kedalam format JSON
    def _json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    # Menampilkan semua data
    @classmethod
    def get(cls):
        return cls.query.order_by(cls.name).all()

    # Menampilkan data berdasarkan id
    @classmethod
    def find(cls, id: int):
        return cls.query.filter_by(id=id).first()

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
