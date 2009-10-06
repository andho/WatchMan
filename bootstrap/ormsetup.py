# -*- coding: utf-8 -*-

from model.Movie import Movie
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Date, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker
import re

engine = create_engine('sqlite:///movies.db')

def createMovie(fullyqualifiedname, moviepath):
    matched = False
    m = re.search(r'(.*)\[(\d{4})](.*)\[(.*)]-(.*)', fullyqualifiedname)
    if m is not None:
        moviename = re.sub(r'\.', ' ', m.group(1))
        year = m.group(2)
        quality = m.group(3)
        language = m.group(4)
        ripper = m.group(5)
        matched = True
    m = re.search(r'(.*)\[(\d{4})](.*)-(.*)', fullyqualifiedname)
    if not matched and m is not None:
        moviename = re.sub(r'\.', ' ', m.group(1))
        year = m.group(2)
        quality = m.group(3)
        ripper = m.group(4)
        language = ''
        matched = True
    m = re.search(r'(.*).(\d{4}).(.*)-(.*)', fullyqualifiedname)
    if not matched and m is not None:
        moviename = re.sub(r'\.', ' ', m.group(1))
        year = m.group(2)
        quality = m.group(3)
        ripper = m.group(4)
        language = ''
        matched = True
    if matched is not True:
        moviename = fullyqualifiedname
        year = ''
        quality = ''
        language = ''
        ripper = ''
    return Movie(fullyqualifiedname, moviename, moviepath, year, quality, ripper, language)

metadata = MetaData()
movies_table = Table('movies', metadata,
    Column('id', Integer, primary_key=True),
    Column('fullyqualifiedname', String),
    Column('name', String),
    Column('path', String),
    Column('year', String),
    Column('quality', String),
    Column('ripper', String),
    Column('language', String)
)

metadata.create_all(engine)

mapper(Movie, movies_table)

Session = sessionmaker(bind=engine)