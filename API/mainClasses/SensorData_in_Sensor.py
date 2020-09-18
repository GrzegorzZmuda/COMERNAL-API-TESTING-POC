from flask_restful import Resource, abort, marshal_with
from API.Models.SensorDataModel import SensorDataModel
from API.authentication import autheniticate
from API.parsers import sensor_data_post_parser, sensor_data_update_parser
from API.Resource_fields import resource_fields_sensor_data

sensor_data_post_args = sensor_data_post_parser()
sensor_data_update_args = sensor_data_update_parser()

class SensorData_in_Sensor(Resource):
    @autheniticate
    @marshal_with(resource_fields_sensor_data)
    def get(self,sensor_id):
        result = SensorDataModel.query.filter_by(sensor_id = sensor_id).all()
        if not result:
            abort(404, message="could not find sensordata with that id")
        return result