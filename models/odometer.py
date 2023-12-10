from datetime import datetime
from providers.mysql import db

class Odometer(db.Model):
    odometer_id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.car_id'), nullable=False)
    odometer_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    odometer_reading = db.Column(db.Float, nullable=False)