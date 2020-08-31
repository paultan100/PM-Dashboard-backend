import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

try:
    database_path = os.environ['DATABASE_URL']
except Exception as e:
    print('Database Path exception: ' + str(e))
    database_path = (
        #"postgres://postgres:Blue84paired.@localhost:5432/reasons_for_hope"
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


class Project(Basic_Model, db.Model):
    __tablename__ = 'project'

    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    owner = Column(String, nullable=False)

    def __init__(self, title, duration, owner):
        self.duration = duration
        self.title = title
        self.owner = owner

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'owner': self.owner,
        }
