from communication.sensor_hub import SensorHub

import utils.colorlogger

if __name__ == "__main__":
    utils.colorlogger.setColoredLogger()
    sensor_hub = SensorHub()
    sensor_hub.start_sniffin(3)
