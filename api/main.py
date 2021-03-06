from flask import Flask
import datetime
from flask_restful import Api
from api.main_classes.SensorData_in_City import SensorData_in_City
from api.main_classes.SensorDataList import SensorDataList
from api.main_classes.CitiesList import CitiesList
from api.main_classes.City import City
from api.main_classes.Sensor import Sensor
from api.main_classes.SensorsList import SensorsList
from api.main_classes.SensorData import SensorData
from api.main_classes.SensorData_in_Sensor import SensorData_in_Sensor
from os import path,remove
from api.models.SensorDataModel import db
from api.main_classes.Sensors_in_City import Sensors_in_City
from flask import request


#starting Flask and config
app= Flask(__name__)
api= Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
from api.error_handlers import bp
app.register_blueprint(bp)

#True if you want to reset database
flag_test=True
if flag_test and path.exists("api/database.db"):
    remove("api/database.db")

if not path.exists("api/database.db"):
    with app.test_request_context():
        db.create_all()
        db.engine.execute("insert into city_model values(0,'first',34); ")
        db.engine.execute("insert into city_model values(1,'second',34); ")
        db.engine.execute("insert into city_model values(2,'third',34); ")
        db.engine.execute("insert into sensor_model values(0,15,12.0,13.0,0); ")
        db.engine.execute("insert into sensor_model values(1,15,12.0,13.0,0); ")
        db.engine.execute("insert into sensor_model values(2,15,12.0,13.0,1); ")
        db.engine.execute("insert into sensor_model values(3,15,12.0,13.0,1); ")
        db.engine.execute("insert into sensor_model values(4,15,12.0,13.0,2); ")
        db.engine.execute("insert into sensor_model values(5,15,12.0,13.0,2); ")
        now = datetime.datetime.utcnow()
        db.engine.execute("insert into sensor_data_model  values(0,15,'2020-09-09 14:11:14.151198',0); ")
        db.engine.execute("insert into sensor_data_model  values(1,15,'2020-09-09 14:11:14.151198',0); ")
        db.engine.execute("insert into sensor_data_model  values(2,15,'2020-09-09 14:11:14.151198',1); ")
        db.engine.execute("insert into sensor_data_model  values(3,15,'2020-09-09 14:11:14.151198',1); ")
        db.engine.execute("insert into sensor_data_model  values(4,15,'2020-09-09 14:11:14.151198',2); ")
        db.engine.execute("insert into sensor_data_model  values(5,15,'2020-09-09 14:11:14.151198',2); ")
        db.engine.execute("insert into sensor_data_model  values(6,15,'2020-09-09 14:11:14.151198',3); ")
        db.engine.execute("insert into sensor_data_model  values(7,15,'2020-09-09 14:11:14.151198',3); ")
        db.engine.execute("insert into sensor_data_model  values(8,15,'2020-09-09 14:11:14.151198',4); ")
        db.engine.execute("insert into sensor_data_model  values(9,15,'2020-09-09 14:11:14.151198',4); ")
        db.engine.execute("insert into sensor_data_model  values(10,15,'2020-09-09 14:11:14.151198',5); ")
        db.engine.execute("insert into sensor_data_model  values(11,15,'2020-09-09 14:11:14.151198',5); ")


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
    app.run(debug=False)