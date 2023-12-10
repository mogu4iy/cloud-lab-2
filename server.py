from flask import Flask, render_template, request, redirect, url_for
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


@app.route('/')
def index():
    cars = Car.query.all()
    return render_template('index.html', cars=cars)

@app.route('/create_car', methods=['GET', 'POST'])
def create_car():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        year = int(request.form['year'])
        fuel_capacity = float(request.form['fuel_capacity'])
        current_odometer = float(request.form['current_odometer'])

        car = Car(brand=brand, model=model, year=year, fuel_capacity=fuel_capacity, current_odometer=current_odometer)
        db.session.add(car)
        db.session.commit()
        
        return redirect(url_for('index'))

    return render_template('create_car.html')

@app.route('/add_refuel/<int:car_id>', methods=['GET', 'POST'])
def add_refuel(car_id):
    if request.method == 'POST':
        car = Car.query.get_or_404(car_id)
        refuel_date = datetime.strptime(request.form['refuel_date'], '%Y-%m-%d')
        fuel_amount = float(request.form['fuel_amount'])
        fuel_price = float(request.form['fuel_price'])
        odometer_reading = float(request.form['odometer_reading'])

        refuel = Refuel(car=car, refuel_date=refuel_date, fuel_amount=fuel_amount, fuel_price=fuel_price, odometer_reading=odometer_reading)
        db.session.add(refuel)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_refuel.html', car_id=car_id)

@app.route('/add_odometer/<int:car_id>', methods=['GET', 'POST'])
def add_odometer(car_id):
    if request.method == 'POST':
        car = Car.query.get_or_404(car_id)
        odometer_date = datetime.strptime(request.form['odometer_date'], '%Y-%m-%d')
        odometer_reading = float(request.form['odometer_reading'])

        odometer = Odometer(car=car, odometer_date=odometer_date, odometer_reading=odometer_reading)
        db.session.add(odometer)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_odometer.html', car_id=car_id)
