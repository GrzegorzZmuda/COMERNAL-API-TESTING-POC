import datetime
from Models.SensorModel import db


class SensorDataModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    temperature = db.Column(db.Integer, nullable= False)
    measurement_datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor_model.id'))

    def __repr__(self):
        return f"SensorData(temperature = {self.temperature}, sensor_id = {self.sensor_id}"