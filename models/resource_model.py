from models.models import db, Basic_Model
from sqlalchemy import Column, String, Integer
import datetime

"""
    This is the basic Resource class
"""
class ResourceManagement(Basic_Model, db.Model):
    __tablename__ = 'resourceManagement'

    projectName = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    resourceName = Column(String, nullable=False)
    status = Column(String, nullable=True)
    updatedDate = Column(db.DateTime, default=datetime.datetime.utcnow,
                         nullable=True)

    def __init__(self, projectName, duration, resourceName, status,
                 updatedDate):
        self.duration = duration
        self.projectName = projectName
        self.resourceName = resourceName
        self.status = status
        self.updatedDate = updatedDate

    def format(self):
        return {
            'id': self.id,
            'projectName': self.projectName,
            'duration': self.duration,
            'resourceName': self.resourceName,
            'status': self.status,
            'updatedDate': self.updatedDate
        }