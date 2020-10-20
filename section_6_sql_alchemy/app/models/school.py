from database import db


class School(db.Model):
    __tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    students = db.relationship('Student', lazy='dynamic')

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    # Memformat data kedalam bentuk json
    def _json(self):
        return {
            'id': self.id,
            'name': self.name,
            'students': [student._json() for student in self.students.all()]
        }

    # Menampilkan semua data
    @classmethod
    def all(cls):
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
