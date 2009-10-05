# -*- coding: utf-8 -*-

class Movie(object):
    def __init__(self, fullyqualifiedname, name, path, year, quality, ripper, language):
        self.fullyqualifiedname = fullyqualifiedname
        self.name = name
        self.path = path
        self.year = year
        self.quality = quality
        self.ripper = ripper
        self.language = language
    
    def __repr__(self):
        return "<Movie('{0}','{1}','{2}','{3}','{4}','{5}','{6}')>".format(
            self.fullyqualifiedname,
            self.name,
            self.path,
            self.year,
            self.quality,
            self.ripper,
            self.language
        )