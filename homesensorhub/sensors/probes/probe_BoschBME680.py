"""Module which implements the probing for the BoschBME680 sensor."""
from sensors.probes.probe_BoschBME import ProbeBoschBME
from sensors.types.BoschBME.BoschBME680_type import TemperatureBoschBME680
from sensors.types.BoschBME.BoschBME680_type import AltitudeBoschBME680
from sensors.types.BoschBME.BoschBME680_type import HumidityBoschBME680
from sensors.types.BoschBME.BoschBME680_type import PressureBoschBME680
from sensors.types.BoschBME.BoschBME680_type import GasBoschBME680

import adafruit_bme680
import logging


logging.basicConfig(level=logging.INFO)


class ProbeBoschBME680(ProbeBoschBME):
    """Class which implements probing for BME680 sensor."""

    def get_sensor_probe_function():
        """Return the function used for probing the sensor."""
        return adafruit_bme680.Adafruit_BME680_I2C

    def get_sensor_name():
        """Return the name of the sensor."""
        return "BoschBME680"

    def generate_sensor_types(sensor):
        return [TemperatureBoschBME680(sensor),
                AltitudeBoschBME680(sensor),
                HumidityBoschBME680(sensor),
                PressureBoschBME680(sensor),
                GasBoschBME680(sensor)]
