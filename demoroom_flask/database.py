# to init the db, run the following commands in venv and run
# 'flask db init'
# 'flask db migrate -m "demos table" ' 
# 'flask db upgrade'
# and then run this script to populate the database
from sys import platform as _platform
from os import listdir, walk, name
from os.path import isfile, join
import itertools
from app import db
from app.models import Demo

text_demos = 'app/static/demos_text/'
names = []
categories = []
texts = []
proper_names = []


def get_names():
    for f in listdir(text_demos):
        names.append(f.replace('.txt', ''))

# Will remove posix newlines ('\n') and replace w/ spaces
def get_texts_posix():
    for f in listdir(text_demos):
        file = open(text_demos + f, 'r')
        currText = file.read().replace('\n', ' ')
        texts.append(currText)

# Windows uses '\r\n' as newline so we need a different version
# of the above if that's what's running
def get_texts_windows():
    for f in listdir(text_demos):
        file = open(text_demos + f, 'r')
        currText = file.read().replace('\r\n', ' ')
        texts.append(currText)

def get_proper_names():
    for f in listdir(text_demos):
        file = open(text_demos + f, 'r')
        currline = " ".join(file.readline().split())
        proper_names.append(currline)

def add_to_db():
    for (a, b, c) in zip(names, texts, proper_names):
        d = Demo(name=a, text=b, proper_name=c)
        db.session.commit()

get_names()
if _platform == "linux" or _plaform == "linux2" or _platform == "darwin":
    get_texts_posix()
elif _platform == "win32" or _platform == "win64":
    get_texts_windows()
else:
    print("Unable to get texts -- platform error")
get_proper_names()
add_to_db()
print(_platform)


