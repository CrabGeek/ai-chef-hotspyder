from chef_nats import settings as nats_settings
import nats

class NatsClient():

    def __init__(self):
        self.__address = nats_settings.NATS_SERVER_ADDRESS
        self.__nc = None

    @property
    def address(self):
        return self.__address
    
    @property
    def connect(self):
        return self.__nc
    

    async def run(self):
        self.__nc = await nats.connect(self.__address)