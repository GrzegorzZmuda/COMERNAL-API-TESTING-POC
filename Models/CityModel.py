from flask_sqlalchemy import SQLAlchemy
from db import db

class CityModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cityname =db.Column(db.String(100),nullable= False)
    inhabitants = db.Column(db.Integer, nullable= False)
    sensors = db.relationship('SensorModel', backref="SensorCity", cascade="all, delete-orphan")

    def __repr__(self):
        return f"City(cityname = {self.cityname}, inhabitants = {self.inhabitants})"