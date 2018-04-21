import attr
import logzero
import trio

from serial import Serial, SerialException
from .util import Instrument, SerialConnectionError


@attr.s
class LockInAmplifier(Instrument):

    """The interface for the lock-in amplifier.

    The lock-in amplifier (LIA) digitizes the signal from the detector and picks out
    the component at the same frequency and at a fixed phase relative to the signal
    provided at the Ref. input.
    """

    _port_settings = attr.ib()
    _logger = attr.ib(default=logzero.logger)
    _ser = attr.ib(init=False, default=None)
    _current_cmd = attr.ib(init=False, default=None)

    async def connect(self, port_settings=None):
        settings = port_settings if port_settings is not None else self._port_settings
        try:
            ser = Serial(**settings)
        except (SerialException, ValueError) as e:
            self._logger.error("Could not connect to LIA port", exc_info=True)
            raise SerialConnectionError

        else:
            self._ser = ser
        self._aser = trio.wrap_file(self._ser)

    async def is_connected(self):
        """Indicate whether the connection to the serial port is open or closed.

        It is possible to be connected without being able to communicate. This
        method only indicates whether the connection is open. The know whether
        communication is possible, see #LockInAmplifier.can_communicate().

        """
        return self._ser.is_open

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

    async def clear_status_bytes(self):
        pass

    async def set_data_channels(self):
        pass

    async def set_ref_source(self):
        pass

    async def set_input_mode(self):
        pass

    async def set_input_coupling(self):
        pass

    async def set_voltage_input_mode(self):
        pass

    async def set_grounding_mode(self):
        pass
