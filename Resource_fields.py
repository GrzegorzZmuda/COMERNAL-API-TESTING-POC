from flask_restful import  fields

resource_fields_sensor = {
    'id': fields.Integer,
    'height': fields.Integer,
    'latitude': fields.Float,
    'longitude': fields.Float,
    'city_id': fields.Integer
}

resource_fields_city_nested = {
    'id': fields.Integer,
    'cityname': fields.String,
    'inhabitants': fields.Integer,
    'sensors': fields.Nested(resource_fields_sensor)
}
resource_fields_city = {
    'id': fields.Integer,
    'cityname': fields.String,
    'inhabitants': fields.Integer,

}
resource_fields_sensor_data = {
    'id': fields.Integer,
    'temperature': fields.Integer,
    'measurement_datetime': fields.DateTime,
    'sensor_id': fields.Integer
}

resource_fields_sensor_nested = {
    'id': fields.Integer,
    'height': fields.Integer,
    'latitude': fields.Float,
    'longitude': fields.Float,
    'city_id': fields.Integer,
    'sensordata': fields.Nested(resource_fields_sensor_data)
}