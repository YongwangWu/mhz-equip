import attr

from .util import Instrument


@attr.s
class LockInAmplifier(Instrument):
    current_cmd = attr.ib(default=None)

    async def connect(self, port_settings=None):
        pass

    async def is_connected(self):
        pass

    async def can_communicate(self):
        pass

    async def get_filter_slope(self):
        pass

    async def set_filter_slope(self, code):
        pass

    async def get_sensitivity(self):
        pass

    async def set_sensitivity(self, code):
        pass

    async def get_input_range(self):
        pass

    async def set_input_range(self, code):
        pass

    async def get_time_constant(self):
        pass

    async def set_time_constant(self, code):
        pass

    async def get_x_signal(self):
        pass

    async def get_x_noise(self):
        pass

    async def get_aux1(self):
        pass

    async def get_aux2(self):
        pass

    async def get_aux3(self):
        pass

    async def get_data_channels_snapshot(self):
        pass

    async def is_locked(self):
        pass

    async def is_overloaded(self):
        pass
