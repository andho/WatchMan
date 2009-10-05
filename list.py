# -*- coding: utf-8 -*-

from ormsetup import *

session = Session()

movie = session.query(Movie).filter_by(filename='scan.py').first()
print movie