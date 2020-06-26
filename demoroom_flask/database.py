# to init the db, run the following commands in venv and run
# 'flask db init'
# 'flask db migrate -m "demos table" ' 
# 'flask db upgrade'
# and then run this script to populate the database

from os import listdir, walk
from os.path import isfile, join
import itertools
from app import db
from app.models import Demo

text_demos = 'app/static/demos_text/'
names = []
categories = []
texts = []
proper_names = []

for f in listdir(text_demos):
    names.append(f.replace('.txt', ''))

for f in listdir(text_demos):
    file = open(text_demos + f, 'r')
    currText = file.read().replace('\n', ' ')
    texts.append(currText)

for f in listdir(text_demos):
    file = open(text_demos + f, 'r')
    currline = " ".join(file.readline().split())
    proper_names.append(currline)

for (a, b, c) in zip(names, texts, proper_names):
    d = Demo(name=a, text=b, proper_name=c)
    db.session.add(d)
    db.session.commit()




