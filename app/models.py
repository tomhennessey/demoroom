from app import db

class DemoRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    demo = db.Column(db.String(128))
    text_field = db.Column(db.String(10000))

    def __repr__(self):
        return '<Request {}>'.format(self.name)

class Demo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    category = db.Column(db.String(256), index=True, unique=False)
    text = db.Column(db.String(10000), index=True, unique=True)
    proper_name = db.Column(db.String(256), index=True, unique=True)

    def __repr__(self):
        return '<Demo {}>'.format(self.name)


