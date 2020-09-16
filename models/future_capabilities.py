from models.models import db, Basic_Model
from sqlalchemy import Column, String, Integer

"""
    This is the basic Resource class
"""
class Future_Capabilities(Basic_Model, db.Model):
    __tablename__ = 'future_capabilities'

    points = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    capabilities_count = Column(Integer, nullable=False)

    def __init__(self, points, size, capabilities_count):
        self.points = points
        self.size = size
        self.capabilities_count = capabilities_count

    def format(self):
        return {
            'id': self.id,
            'points': self.points,
            'size': self.size,
            'capabilities_count': self.capabilities_count
        }