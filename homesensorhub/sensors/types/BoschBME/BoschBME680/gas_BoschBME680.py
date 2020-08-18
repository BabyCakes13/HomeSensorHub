"""Module which implements the Bosch680BME gas sensor module set up."""
from sensors.types.gas import Gas


class GasBoschBME680(Gas):
    """Class which implements the gas collected from BoschBME680 sensor module."""

    MEASURE = 'Meters'
    SENSOR_NAME = 'BoschBME680'

    def __init__(self, sensor):
        """
        Initialise the gas.

        The object is initialised with the physical sensor responsable for providing values of this
        type. As an example, the name can be "BoschBME680".
        """
        self.__sensor = sensor

    def get_sensor_name(self) -> str:
        """
        Return the actual name of the sensor (eg. BME680, BME680 etc.).

        :return: string
        """
        return self.SENSOR_NAME

    def get_sensor_value(self) -> int:
        """
        Return the value collected by the sensor.

        :return: int
        """
        return self.__sensor.gas

    def get_sensor_measure(self) -> str:
        """
        Return the unit of measurement for the gas for this sensor module.

        :return: string
        """
        return GasBoschBME680.MEASURE