# -*- coding: utf-8 -*-

import os, shutil, glob
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker

engine = create_engine('sqlite:///movies.db')

class Movie(object):
    def __init__(self, filename):
        self.filename
    
    def __repr__(self):
        return "<Movie('{0}')>".format(self.filename)
    



metadata = MetaData()
movies_table = Table('movies', metadata,
    Column('id', Integer, primary_key=True),
    Column('fullname', String)
)

metadata.create_all(engine)

mapper(Movie, movies_table)

