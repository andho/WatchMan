# -*- coding: utf-8 -*-

from ormsetup import *
import os, hashlib

def scan():
    session = Session()
    
    path = 'D:/movies'
    hashfile = 'hashfile'
    filelist = os.listdir(path)
    newhash = hashlib.md5(str(filelist)).digest()
    hashfile = open('./.hashfile', 'r')
    hash = hashfile.read()
    hashfile.close()
    
    movies = []
    if hash != newhash:
        hashfile = open('./.hashfile', 'w')
        hashfile.write(newhash)
        hashfile.close()
        print "Directory structure changed"
        for file in filelist:
            if os.path.isdir(path + '/' + file):
                moviedir = os.listdir(path + '/' + file)
                moviepath = "(no movie file)"
                for dirfile in moviedir:
                    if dirfile.endswith(('.avi','.mkv','.mp4','.wmv')):
                        moviepath = path + '/' + file + '/' + dirfile
                        break
                moviename = file
            elif file.endswith(('.avi', '.mkv', '.mp4', '.wmv')):
                moviepath = path + '/' + file
                moviename = file[0:-4]
    
            movie = session.query(Movie).filter_by(fullyqualifiedname=moviename).first()
            if movie is None:
                movie = createMovie(moviename, moviepath)
                if movie is not False:
                    movies.append(movie)
    
    if len(movies) > 0:
        session.add_all(movies)
    print session.new
    session.commit()

def emptyTheLibrary():
    session = Session()
    for movie in session.query(Movie):
        session.delete(movie)
    session.commit()

def getMovieList():
    session = Session()
    return session.query(Movie).all()