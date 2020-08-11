#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.orm import scoped_session


class DBStorage():
    """ SQL storage class """
    __engine = None
    __session = None

    def __init__(self):
        db_user = os.environ.get('HBNB_MYSQL_USER')
        db_password = os.environ.get('HBNB_MYSQL_PWD')
        db_host = os.environ.get('HBNB_MYSQL_HOST')
        db_name = os.environ.get('HBNB_MYSQL_DB')
        mode = os.environ.get('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(db_user,
                                             db_password, db_host,
                                             db_name), pool_pre_ping=True)
        if (mode == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ This must return a dictionary: with all the methods """
        if cls is None:
            return (DBStorage.__session)
        else:
            cls_dict = {}
            for key, value in DBStorage.__session.items():
                if type(value) == cls:
                    cls_dict[key] = value
            return cls_dict

    def new(self, obj):
        """ create a new object """
        self.__session.add(obj)

    def save(self):
        """ saves session in database """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes an obj from db """
        if not obj:
            return
        # key = str(obj.__class__.__name__)
        self.__session.delete(obj)
        # search = self.__session.query(key)
        # for data in search:
        #    if obj is data:
        #        self.__session.delete(data)

    def reload(self):
        """ loads all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        Session = scoped_session(session_maker)
        self.__session = Session()
