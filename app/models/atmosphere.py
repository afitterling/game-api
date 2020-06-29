from extensions import db
from builtins import classmethod
from sqlalchemy.dialects.postgresql import JSON

class Atmosphere(db.Model):
    __tablename__ = 'atmospheres'

    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer)
    gases = db.Column(JSON)
    #items = db.relationship('Item', backref='user')

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

