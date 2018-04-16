from abc import ABCMeta, abstractmethod


class SerialConnectionError(Exception):
    pass


class Instrument(metaclass=ABCMeta):

    """The bare minimum interface that all instruments should implement.

    """

    @abstractmethod
    async def connect(self, port_settings=None):
        pass

    @abstractmethod
    async def is_connected(self):
        pass

    @abstractmethod
    async def can_communicate(self):
        pass
