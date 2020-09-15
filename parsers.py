from flask_restful import reqparse, inputs

def city_post_parser():
    city_post_args = reqparse.RequestParser()
    city_post_args.add_argument("cityname", type=str, help="Name of the city is required", required=True)
    city_post_args.add_argument("inhabitants", type=int, help="Number of inhabitants required", required=True)
    return city_post_args

def city_update_parser():
    city_update_args = reqparse.RequestParser()
    city_update_args.add_argument("cityname", type=str, help="Name of the city")
    city_update_args.add_argument("inhabitants", type=int, help="Number of inhabitants")
    return city_update_args

def sensor_post_parser():
    sensor_post_args = reqparse.RequestParser()
    sensor_post_args.add_argument("height", type=int, help="Height of the sensor is required", required=True)
    sensor_post_args.add_argument("latitude", type=float, help="Latitude of the sensor is required", required=True)
    sensor_post_args.add_argument("longitude", type=float, help="Longitude of the sensor is required", required=True)
    sensor_post_args.add_argument("city_id", type=int, help="city_id of the sensor is required", required=True)
    return sensor_post_args

def sensor_update_parser():
    sensor_update_args = reqparse.RequestParser()
    sensor_update_args.add_argument("height", type=int, help="Height of the sensor")
    sensor_update_args.add_argument("latitude", type=float, help="Latitude of the sensor")
    sensor_update_args.add_argument("longitude", type=float, help="Longitude of the sensor")
    sensor_update_args.add_argument("city_id", type=int, help="city_id of the sensor")
    return sensor_update_args

def sensor_data_post_parser():
    sensor_data_post_args = reqparse.RequestParser()
    sensor_data_post_args.add_argument("sensor_id", type=int, help="sensor_id of the sensordata is required",
                                      required=True)
    sensor_data_post_args.add_argument("measurement_datetime",
                                      type=inputs.datetime_from_iso8601,
                                      help="datetime of measurment",
                                      required=False)
    sensor_data_post_args.add_argument("temperature", type=int, help="measured temperature is required", required=True)
    return sensor_data_post_args

def sensor_data_update_parser():
    sensor_data_update_args = reqparse.RequestParser()
    sensor_data_update_args.add_argument("sensor_id", type=int, help="sensor_id of the sensordata")
    sensor_data_update_args.add_argument("measurement_datetime",
                                         type=inputs.datetime_from_iso8601,
                                         help="datetime of measurment")
    sensor_data_update_args.add_argument("temperature", type=int, help="measured temperature")
    return sensor_data_update_args