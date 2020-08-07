"""Module which implements the payload class."""
import json


class Payload:
    """Class which implements the configuration of the payload for MQTT."""

    def __init__(self, type, name, value, timestamp, measurement):
        """Extract and structure the data received from the sensors."""
        self.__type = type
        self.__name = name
        self.__value = value
        self.__timestamp = timestamp
        self.__measurement = measurement

    def get_json_payload(self) -> json.dumps:
        """
        Construct the json payload based on the collected data.

        The accepted values for MQTT payload are None, Int, Float and str, so
        before trying to send the raw data from the sensors through MQTT, it
        needs to be refined into an accepted form.
        """
        payload = {
            'type': self.__get_str_type(),
            'name': self.__get_str_name(),
            'value': self.__get_str_value(),
            'timestamp': self.__get_str_timestamp(),
            'measurement': self.__get_str_measurement()
        }

        json_payload = json.dumps(payload,
                                  indent=4,
                                  separators=(". ", " = "),
                                  sort_keys=True)
        return json_payload

    def __get_str_type(self) -> str:
        return str(self.__type)

    def __get_str_name(self) -> str:
        return str(self.__name)

    def __get_str_value(self) -> str:
        return "{}".format(round(self.__value, 2))

    def __get_str_timestamp(self) -> str:
        return str(self.__timestamp)

    def __get_str_measurement(self) -> str:
        return str(self.__measurement)

    def get_value(self):
        """Return the value of the sensor."""
        return self.__value

    def get_type(self):
        """
        Return the type of the sensor.

        Needed for topic creation in MQTT.
        """
        return self.__type