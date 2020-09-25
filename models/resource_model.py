from models.models import db, Basic_Model
from sqlalchemy import Column, String, Integer
import datetime

"""
    This is the basic Resource class
"""
class ResourceManagement(Basic_Model, db.Model):
    __tablename__ = 'resourceManagement'

    projectName = Column(String, nullable=False)
    resourceName = Column(String, nullable=False)
    status = Column(String, nullable=True)
    updatedDate = Column(db.DateTime, default=datetime.datetime.utcnow,
                         nullable=True)
    roles = Column (String, default="N/A", nullable=False)

    def __init__(self, projectName, roles, resourceName, status,
                 updatedDate):
        self.projectName = projectName
        self.resourceName = resourceName
        self.status = status
        self.updatedDate = updatedDate
        self.roles = roles

    def format(self):
        return {
            'id': self.id,
            'projectName': self.projectName,
            'roles': self.roles,
            'resourceName': self.resourceName,
            'status': self.status,
            'updatedDate': self.updatedDate
        }