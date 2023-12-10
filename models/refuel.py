from datetime import datetime
from providers.mysql import db

class Refuel(db.Model):
    refuel_id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.car_id'), nullable=False)
    refuel_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    fuel_amount = db.Column(db.Float, nullable=False)
    fuel_price = db.Column(db.Float, nullable=False)
    odometer_reading = db.Column(db.Float, nullable=False)