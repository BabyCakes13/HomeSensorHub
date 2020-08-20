import paho.mqtt.client as mqtt
import socket
import os
import getpass
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


class Singleton(type):
    """Generic singleton pattern for classes."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MQTT(metaclass=Singleton):
    """Create and hold connection through MQTT."""

    def __init__(self, broker_url="mqtt.tinker.haus", broker_port=1883):
        self.__client = mqtt.Client()
        self.__client.on_message = self.on_message
        self.__client.on_connect = self.on_connect

        self.__broker_url = broker_url
        self.__broker_port = broker_port

        self.__hostname = socket.gethostname() + "/"
        self.__dev = getpass.getuser() + "/"
        if os.getuid() == 0:
            self.__dev = ""
        self.__topic_base = self.__dev + self.__hostname

        self.connect()

    def connect(self):
        try:
            connection = self.__client.connect_async(self.__broker_url,
                                                     self.__broker_port)
            self.__client.loop_start()
            logging.info("MQTT connection result: {}".format(connection))
            return True
        except ConnectionRefusedError as error:
            logging.error("MQTT connect refused: {}".format(error))
            return False

    def on_message(self, client, userdata, message):
        print("{}; {}; {}.".format(client, userdata, message))

    def on_connect(self, client, userdata, flags, rc):
        logging.info("Succesfully connected to {}".format(self.__broker_url))

    def get_topic_base(self):
        """Return topic base used for publish."""
        return self.__topic_base

    def get_client(self):
        return self.__client

    def get_broker_url(self):
        return self.__broker_url
