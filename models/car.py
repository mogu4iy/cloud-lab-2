from providers.mysql import db
from dataclasses import dataclass

@dataclass
class Car(db.Model):
    id: int
    brand: str
    model: str
    year: int
    fuel_capacity: float
    current_odometer: float

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    fuel_capacity = db.Column(db.Float, nullable=False)
    current_odometer = db.Column(db.Float, nullable=False)