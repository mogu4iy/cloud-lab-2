from providers.mysql import db

class Car(db.Model):
    car_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    fuel_capacity = db.Column(db.Float, nullable=False)
    current_odometer = db.Column(db.Float, nullable=False)