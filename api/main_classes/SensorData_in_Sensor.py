from flask_restful import Resource, abort, marshal_with
from api.models.SensorDataModel import SensorDataModel
from api.authentication import autheniticate
from api.parsers import sensor_data_post_parser, sensor_data_update_parser
from api.resource_fields import resource_fields_sensor_data

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