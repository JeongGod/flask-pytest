from db_connect import db


class user(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    user_id    = db.Column(db.String(50), primary_key=True)
    user_pw    = db.Column(db.String(255), nullable=False)
    introduce   = db.Column(db.String(255))

    def __init__(self, user_id, user_pw):
        self.user_id   = user_id
        self.user_pw   = user_pw
    
