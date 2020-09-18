from flask_restful import Resource, abort, marshal_with
from API.Models.CityModel import CityModel
from API.Models.SensorDataModel import db
from API.Models.SensorModel import SensorModel
from API.authentication import autheniticate
from API.parsers import sensor_post_parser, sensor_update_parser
from API.Resource_fields import resource_fields_sensor_nested, resource_fields_sensor

sensor_post_args = sensor_post_parser()
sensor_update_args = sensor_update_parser()

class Sensor(Resource):
    @autheniticate
    @marshal_with(resource_fields_sensor_nested)
    def get(self,sensor_id):
        result = SensorModel.query.filter_by(id=sensor_id).first()
        if not result:
            abort(404, message="could not find sensor with that id")
        return result

    @autheniticate
    @marshal_with(resource_fields_sensor)
    def put(self, sensor_id):
        args = sensor_update_args.parse_args()
        result = SensorModel.query.filter_by(id=sensor_id).first()
        if not result:
            abort(404, message="Sensor doesn't exist, cannot update")
        if args['city_id'] or args['city_id'] == 0 :
            result1 = CityModel.query.filter_by(id=args['city_id']).first()
            if not result1:
                abort(404, message="could not find city with that id")
        if args['height']:
            result.height = args['height']
        if args['latitude']:
            result.latitude = args['latitude']
        if  args['longitude']:
            result.longitude= args['longitude']
        if args['city_id'] or args['city_id'] == 0:
            result.city_id = args['city_id']
        db.session.commit()
        return result

    @autheniticate
    def delete(self,sensor_id):
        result = SensorModel.query.filter_by(id=sensor_id).first()
        if not result:
            abort(404, message="could not find sensor with that id")
        db.session.delete(result)
        db.session.commit()
        return '',204