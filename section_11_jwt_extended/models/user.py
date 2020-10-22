from database import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, _id, name, email, password):
        self.id = _id
        self.name = name
        self.email = email
        self.password = password

    # Memformat data kedalam JSON
    def _json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

    # Menampilkan data berdasarkan id
    @classmethod
    def find(cls, _id):
        return cls.query.filter_by(id=_id).first()

    # Menampilkan data berdasarkan email
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    # Menyimpan data
    def save(self):
        db.session.add(self)
        db.session.commit()
        return None
