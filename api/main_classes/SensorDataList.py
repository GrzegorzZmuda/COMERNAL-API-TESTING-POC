from flask_restful import Resource, abort, marshal_with
from api.models.SensorDataModel import SensorDataModel
from api.models.SensorDataModel import db
from api.models.SensorModel import SensorModel
from api.authentication import autheniticate
from api.parsers import sensor_data_post_parser, sensor_data_update_parser
from api.resource_fields import resource_fields_sensor_data

sensor_data_post_args = sensor_data_post_parser()
sensor_data_update_args = sensor_data_update_parser()

class SensorDataList(Resource):
    @autheniticate
    @marshal_with(resource_fields_sensor_data)
    def get(self):
        result = SensorDataModel.query.all()
        if not result:
            abort(404, message="could not find sensordata with that id")
        return result

    @autheniticate
    @marshal_with(resource_fields_sensor_data)
    def post(self):
        args = sensor_data_post_args.parse_args()
        result = SensorModel.query.filter_by(id=args['sensor_id']).first()
        if not result:
            abort(404, message="could not find sensor with that id")
        sensordata = SensorDataModel(temperature=args['temperature'],
                                     sensor_id=args['sensor_id'],
                                     measurement_datetime=args['measurement_datetime'])
        db.session.add(sensordata)
        db.session.commit()
        return sensordata, 201