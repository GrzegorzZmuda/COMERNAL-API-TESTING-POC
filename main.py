from flask import Flask
from flask_restful import Api
from mainClasses.SensorData_in_City import SensorData_in_City
from mainClasses.SensorDataList import SensorDataList
from mainClasses.CitiesList import CitiesList
from mainClasses.City import City
from mainClasses.Sensor import Sensor
from mainClasses.SensorsList import SensorsList
from mainClasses.SensorData import SensorData
from mainClasses.SensorData_in_Sensor import SensorData_in_Sensor
from os import path
from Models.SensorDataModel import db
from mainClasses.Sensors_in_City import Sensors_in_City


#starting Flask and config
app= Flask(__name__)
api= Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
from error_handlers import bp
app.register_blueprint(bp)


if not path.exists("database.db"):
    with app.test_request_context():
        db.create_all()

#adresses
api.add_resource(CitiesList,'/city')
api.add_resource(City,'/city/<int:city_id>')
api.add_resource(Sensors_in_City,'/city/<int:city_id>/sensor')
api.add_resource(SensorsList,'/sensor',
                 '/city/sensor')
api.add_resource(Sensor,'/sensor/<int:sensor_id>',
                 '/city/sensor/<int:sensor_id>')
api.add_resource(SensorDataList,'/sensordata','/sensor/sensordata',
                 '/city/sensor/sensordata')
api.add_resource(SensorData_in_Sensor,'/sensor/<int:sensor_id>/sensordata',
                 '/city/sensor/<int:sensor_id>/sensordata')
api.add_resource(SensorData,'/sensordata/<int:sensor_data_id>',
                 '/sensor/sensordata/<int:sensor_data_id>',
                 '/city/sensor/sensordata/<int:sensor_data_id>')
api.add_resource(SensorData_in_City,
                 '/city/<int:city_id>/sensor/sensordata')


#run server (debug)
if __name__ == "__main__":
    app.run(debug=True)