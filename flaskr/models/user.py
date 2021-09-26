from flaskr import db


class user(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    racer_id    = db.Column(db.String(50), primary_key=True, nullable=False)
    racer_pw    = db.Column(db.String(255), nullable=False)
    racer_name  = db.Column(db.String(20), nullable=False)
    introduce   = db.Column(db.String(255))

    def __init__(self, racer_id, racer_pw, racer_name):
        self.racer_id   = racer_id
        self.racer_pw   = racer_pw
        self.racer_name = racer_name
    
