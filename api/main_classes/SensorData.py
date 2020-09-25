from flask_restful import Resource, abort, marshal_with
from api.models.SensorDataModel import SensorDataModel
from api.models.SensorDataModel import db
from api.models.SensorModel import SensorModel
from api.authentication import autheniticate
from api.parsers import sensor_data_post_parser, sensor_data_update_parser
from api.resource_fields import resource_fields_sensor_data

sensor_data_post_args = sensor_data_post_parser()
sensor_data_update_args = sensor_data_update_parser()

class SensorData(Resource):
    @autheniticate
    @marshal_with(resource_fields_sensor_data)
    def get(self,sensor_data_id):
            result = SensorDataModel.query.filter_by(id=sensor_data_id).first()
            if not result:
                abort(404, message="could not find sensordata with that id")
            return result


    @autheniticate
    @marshal_with(resource_fields_sensor_data)
    def put(self, sensor_data_id):
        args = sensor_data_update_args.parse_args()
        result = SensorDataModel.query.filter_by(id=sensor_data_id).first()
        if not result:
            abort(404, message="SensorData doesn't exist, cannot update")
        if args['sensor_id'] or args['sensor_id'] == 0 :
            result1 = SensorModel.query.filter_by(id=args['sensor_id']).first()
            if not result1:
                abort(404, message="could not find sensor with that id")
        if args['temperature']:
            result.temperature = args['temperature']
        if args['sensor_id'] or args['sensor_id'] == 0:
            result.sensor_id = args['sensor_id']
        if  args['measurement_datetime']:
            result.measurement_datetime= args['measurement_datetime']

        db.session.commit()
        return result

    @autheniticate
    def delete(self,sensor_data_id):
            result = SensorDataModel.query.filter_by(id=sensor_data_id).first()
            if not result:
                abort(404, message="could not find sensordata with that id")
            db.session.delete(result)
            db.session.commit()
            return '',204