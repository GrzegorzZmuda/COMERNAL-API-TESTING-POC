from flask_restful import Resource, abort, marshal_with
from Models.SensorModel import SensorModel
from authentication import autheniticate
from parsers import sensor_post_parser, sensor_update_parser
from Resource_fields import resource_fields_sensor

sensor_post_args = sensor_post_parser()
sensor_update_args = sensor_update_parser()

class Sensors_in_City(Resource):

    @autheniticate
    @marshal_with(resource_fields_sensor)
    def get(self,city_id):
        result = SensorModel.query.filter_by(city_id = city_id).all()
        if not result:
            abort(404, message="could not find sensor with that id")
        return result