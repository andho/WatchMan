# -*- coding: utf-8 -*-

from bootstrap.ormsetup import *
from model import Service

#Service.scan()
#Service.emptyTheLibrary()
print Service.getMovieList()