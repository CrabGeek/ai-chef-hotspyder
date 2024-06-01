from .. import settings
import nats

class NatsClient():

    def __init__(self):
        self.__address = settings.NATS_SERVER_ADDRESS
        self.__nc = None

    