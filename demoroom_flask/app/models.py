from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Demo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    category = db.Column(db.String(256), index=True, unique=False)
    text = db.Column(db.String(10000), index=True, unique=True)
    proper_name = db.Column(db.String(256), index=True, unique=True)

    def __repr__(self):
        return '<Demo {}>'.format(self.name)
