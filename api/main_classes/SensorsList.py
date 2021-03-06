from flask_restful import Resource, abort, marshal_with
from api.models.CityModel import CityModel
from api.models.SensorDataModel import db
from api.models.SensorModel import SensorModel
from api.authentication import autheniticate
from api.parsers import sensor_post_parser, sensor_update_parser
from api.resource_fields import resource_fields_sensor

sensor_post_args = sensor_post_parser()
sensor_update_args = sensor_update_parser()

class SensorsList(Resource):

    @autheniticate
    @marshal_with(resource_fields_sensor)
    def get(self):
        result = SensorModel.query.all()
        if not result:
            abort(404, message="could not find sensor with that id")
        return result

    @autheniticate
    @marshal_with(resource_fields_sensor)
    def post(self):
        args = sensor_post_args.parse_args()
        result = CityModel.query.filter_by(id=args['city_id']).first()
        if not result:
            abort(404, message="could not find city with that id")
        sensor = SensorModel( height=args['height'], latitude=args['latitude'],longitude=args['longitude'], city_id=args['city_id'])
        db.session.add(sensor)
        db.session.commit()
        return sensor, 201