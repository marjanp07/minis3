
from complaint_system import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
class police_station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Coloumn(db.String )



    def __repr__(self):
        return '<User %r>' % self.username