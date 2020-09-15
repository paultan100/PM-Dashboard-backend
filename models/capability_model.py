from models.models import db, Basic_Model
from sqlalchemy import Column, String, Integer

# A capablity class
class Capability(Basic_Model, db.Model):
    __tablename__ = 'capability'

    number = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    size = Column(String, nullable=False)
    status = Column(String, nullable=False)
    length = Column(Integer, nullable=False)
    dependency = Column(String, nullable=False, 
                        default="N/A")

    def __init__(self, number, name, size, status, length,
                 dependency):
        self.number = number
        self.name = name
        self.size = size
        self.status = status
        self.length = length
        self.dependency = dependency

    def format(self):
        return {
            'id': self.id,
            'number': self.number,
            'name' : self.name,
            'size': self.size,
            'length': self.length,
            'status': self.status,
            'dependancy' : self.dependency
        }