from flask import Flask, render_template, request, redirect, url_for, jsonify
from models.car import Car
from models.refuel import Refuel
from models.odometer import Odometer
from providers.mysql import db
from datetime import datetime

app = Flask(__name__)

# Configure databases
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hu2nomejxeylnvo8:lvev1fb5zoxs64h3@i54jns50s3z6gbjt.chr7pe7iynqr.eu-west-1.rds.amazonaws.com/gn9qnb720ln1pd15'

# Initialize databases
db.init_app(app)

@app.route('/car', methods=['POST'])
def create_car():
    brand = request.json['brand']
    model = request.json['model']
    year = int(request.json['year'])
    fuel_capacity = float(request.json['fuel_capacity'])
    current_odometer = float(request.json['current_odometer'])

    car = Car(brand=brand, model=model, year=year, fuel_capacity=fuel_capacity, current_odometer=current_odometer)
    db.session.add(car)
    db.session.commit()

    return jsonify(car)


@app.route('/car/<int:car_id>', methods=['GET'])
def read_car(car_id):
    car = db.get_or_404(Car, {"id": car_id})

    return jsonify(car)


@app.route('/car/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    car = db.get_or_404(Car, {"id": car_id})

    car.brand = request.json['brand']
    car.model = request.json['model']
    car.year = int(request.json['year'])
    car.fuel_capacity = float(request.json['fuel_capacity'])
    db.session.commit()

    return jsonify(car)


@app.route('/car/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    car = db.get_or_404(Car, {"id": car_id})

    db.session.delete(car)
    db.session.commit()

    return jsonify(id = car.id)


@app.route('/car/<int:car_id>/reset', methods=['POST'])
def reset_car(car_id):
    car = db.get_or_404(Car, {"id": car_id})

    date = datetime.now()

    odometer = Odometer(value=car.current_odometer, date=date, is_reseted=True, car_id=car_id)
    db.session.add(odometer)
    db.session.commit()

    car.current_odometer = 0
    db.session.commit()

    return jsonify(car)


@app.route('/refuel', methods=['POST'])
def create_refuel():
    car_id = int(request.json['car_id'])

    car = db.get_or_404(Car, {"id": car_id})

    amount = float(request.json['amount'])
    price = float(request.json['price'])
    date = datetime.strptime(request.json['date'], '%Y-%m-%d %H:%M:%S')
    odometer_value = float(request.json['odometer_value'])

    odometer = Odometer(value=odometer_value, date=date, car_id=car_id)
    db.session.add(odometer)
    db.session.commit()

    refuel = Refuel(car_id=car_id, amount=amount, price=price, date=date, odometer_id=odometer.id)
    db.session.add(refuel)
    db.session.commit()

    car.current_odometer = odometer_value
    db.session.commit()

    return jsonify(refuel)


@app.route('/refuel/<int:refuel_id>', methods=['GET'])
def read_refuel(refuel_id):
    refuel = db.get_or_404(Refuel, {"id": refuel_id})

    return jsonify(refuel)


# @app.route('/refuel/<int:refuel_id>', methods=['PUT'])
# def update_refuel(refuel_id):
#     refuel = db.get_or_404(Refuel, {"id": refuel_id})
#
#     refuel.amount = float(request.json['amount'])
#     refuel.price = float(request.json['price'])
#     db.session.commit()
#
#     return jsonify(refuel)


# @app.route('/refuel/<int:refuel_id>', methods=['DELETE'])
# def delete_refuel(refuel_id):
#     refuel = db.get_or_404(Refuel, {"id": refuel_id})
#
#     db.session.delete(refuel)
#     db.session.commit()
#
#     return jsonify(id = refuel.id)


@app.route('/odometer', methods=['POST'])
def create_odometer():
    car_id = int(request.json['car_id'])

    car = db.get_or_404(Car, {"id": car_id})

    date = datetime.strptime(request.json['date'], '%Y-%m-%d %H:%M:%S')
    value = float(request.json['value'])
    is_reseted = bool(request.json['is_reseted'])

    odometer = Odometer(value=value, date=date, is_reseted=is_reseted, car_id=car_id)
    db.session.add(odometer)
    db.session.commit()

    if is_reseted:
        car.current_odometer = 0
    else:
        car.current_odometer = value
    db.session.commit()

    return jsonify(odometer)


@app.route('/odometer/<int:odometer_id>', methods=['GET'])
def read_odometer(odometer_id):
    odometer = db.get_or_404(Odometer, {"id": odometer_id})

    return jsonify(odometer)


# @app.route('/odometer/<int:odometer_id>', methods=['PUT'])
# def update_odometer(odometer_id):
#     odometer = db.get_or_404(Odometer, {"id": odometer_id})
#
#     odometer.value = float(request.json['value'])
#     db.session.commit()
#
#     return jsonify(odometer)


# @app.route('/odometer/<int:odometer_id>', methods=['DELETE'])
# def delete_odometer(odometer_id):
#     odometer = db.get_or_404(Odometer, {"id": odometer_id})
#
#     db.session.delete(odometer)
#     db.session.commit()
#
#     return jsonify(id = odometer.id)