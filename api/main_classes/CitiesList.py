from flask_restful import Resource, abort, marshal_with
from api.models.CityModel import CityModel
from api.models.SensorDataModel import db
from api.authentication import autheniticate
from api.parsers import city_update_parser, city_post_parser
from api.resource_fields import resource_fields_city

city_post_args = city_post_parser()
city_update_args =city_update_parser()

class CitiesList(Resource):

    @autheniticate
    @marshal_with(resource_fields_city)
    def get(self):
        result = CityModel.query.all()
        if not result:
            abort(404, message="could not find city with that id")
        return result

    @autheniticate
    @marshal_with(resource_fields_city)
    def post(self):
        args = city_post_args.parse_args()
        city = CityModel(cityname=args['cityname'], inhabitants=args['inhabitants'])
        db.session.add(city)
        db.session.commit()
        return city, 201