from models import Basic_Model, db
from sqlalchemy import Column, Integer

class Scope(Basic_Model, db.Model):
    __tablename__ = 'scope'

    week = Column(Integer, nullable=False)
    low = Column(Integer, nullable=False)
    average = Column(Integer, nullable=False)
    high = Column(Integer, nullable=True)
    points = Column(Integer, nullable=True)

    def __init__(self, week, low, average, high,
                 points):
        self.week = week
        self.low = low
        self.average = average
        self.high = high
        self.points = points
    
    def format(self):
        return {
            'id': self.id,
            'week': self.week,
            'low': self.low,
            'average': self.average,
            'high': self.high,
            'points': self.points
        }