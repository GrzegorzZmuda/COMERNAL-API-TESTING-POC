from flask_restful import Resource,abort , marshal_with
from API.Models.CityModel import CityModel
from API.parsers import city_update_parser, city_post_parser
from API.authentication import autheniticate
from API.Models.SensorDataModel import db
from API.Resource_fields import resource_fields_city_nested,resource_fields_city


city_post_args = city_post_parser()
city_update_args =city_update_parser()

class City(Resource):

    @autheniticate
    @marshal_with(resource_fields_city_nested)
    def get(self,city_id):

        result = CityModel.query.filter_by(id=city_id).first()
        if not result:
            abort(404, message="could not find city with that id")
        return result



    @autheniticate
    @marshal_with(resource_fields_city)
    def put(self,city_id):
        args = city_update_args.parse_args()
        result = CityModel.query.filter_by(id=city_id).first()
        if not result:
            abort(404, message="City doesn't exist, cannot update")
        if args['cityname']:
            result.cityname = args['cityname']
        if args['inhabitants']:
            result.inhabitants = args['inhabitants']
        db.session.commit()
        return result

    @autheniticate
    def delete(self,city_id):
        result = CityModel.query.filter_by(id=city_id).first()
        if not result:
            abort(404, message="could not find city with that id")
        db.session.delete(result)
        db.session.commit()
        return '',204