from datetime import datetime
from database import db

class Device(db.Model):

    __tablename__ = 'devices'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    device_no = db.Column(db.Integer, primary_key=False)
    device_test_no = db.Column(db.Integer, primary_key=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
