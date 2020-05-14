import logging as lg
import time

from communication.data_sender import DataSender
from sensors.environmental_sensor import EnvironmentalSensor

class SensorHub:
    """
    Class which will hold the information of all the types of sensors and their data. This will represent the data
    communicator.
    """

    def __init__(self):
        self.data = {}
        self.logging = lg.getLogger(self.__class__.__name__)

        self.environmental_sensors = EnvironmentalSensor()

        self.all_sensors = [self.environmental_sensors]
        # TODO use getattr to iterate only over the sensors instead of hardcoding them into a list.

    def get_data(self):
        return self.data

    def collect_data_from(self, sensor_type) -> None:
        """
        Since all of the types (eg. environmental, motion, light) can have multiple sensors, over a call we get the data
        from all the type's sensors, for now.
        """
        for sensor in sensor_type.sensors:
            data = sensor.get_data()
            self.data.update(data)

    def collect_all_data(self) -> None:
        # TODO Fix the multiple sensors data. When a sensor type has multiple sensors, it actually overwrites the last
        # value rather than having different values for different sensors
        self.logging.info("Collecting all data...")
        for sensor in self.all_sensors:
            self.collect_data_from(sensor)

    def start_sniffin(self, interval):
        ds = DataSender()

        self.logging.info("Started sniffin...")
        while True:
            self.collect_all_data()
            data = self.get_data()
            ds.send_data(data)
            time.sleep(interval)

