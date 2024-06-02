from chef_nats import settings as nats_settings
import nats
import asyncio


class NatsClient:

    nc = None

    def __init__(self):
        self.__address = nats_settings.NATS_SERVER_ADDRESS
        self.__nc = None

    @property
    def address(self):
        return self.__address

    async def run(self):
        NatsClient.nc = await nats.connect(servers=[self.__address])

    @staticmethod
    async def send(subject: str, data: bytes):
        if NatsClient.nc is None:
            return
        await NatsClient.nc.publish(subject=subject, payload=data)

