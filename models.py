import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import datetime

try:
    database_path = os.environ['DATABASE_URL']
except Exception as e:
    print('Database Path exception: ' + str(e))
    database_path = (
        "postgres://postgres:Blue84paired.@localhost:5432/pm_dashboard"
    )

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


"""
    This is the base model which handles inserting,
    updating, and deleting. These methods will be available for
    each class which inherits this basic model.
"""
class Basic_Model():
    id = Column(Integer, primary_key=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


"""
    This is the basic Project class
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
