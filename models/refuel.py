from datetime import datetime
from providers.mysql import db
from dataclasses import dataclass

@dataclass
class Refuel(db.Model):
    id: int
    car_id: int
    odometer_id: int
    date: str
    amount: float
    price: float

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    odometer_id = db.Column(db.Integer, db.ForeignKey('odometer.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
