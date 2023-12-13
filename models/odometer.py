from datetime import datetime
from providers.mysql import db
from dataclasses import dataclass

@dataclass
class Odometer(db.Model):
    id: int
    car_id: int
    date: str
    value: float
    is_reseted: bool

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    value = db.Column(db.Float, nullable=False)
    is_reseted = db.Column(db.Boolean, nullable=True, default=False)