from Models.CityModel import db

class SensorModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    height = db.Column(db.Integer, nullable= False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city_model.id'))
    sensordata = db.relationship('SensorDataModel', backref="SensorData", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Sensor(height = {self.height}, latitude = {self.latitude}, longitude={self.longitude}, city_id={self.city_id})"