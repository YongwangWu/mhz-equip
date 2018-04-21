import subprocess
import time

import pytest
import trio

from serial import Serial
from mhz_equip.lockin import LockInAmplifier


@pytest.fixture(scope="session")
def socat():
    port1 = "/tmp/port1"
    port2 = "/tmp/port2"
    args = ["socat", f"pty,rawer,echo=0,link={port1}", f"pty,rawer,echo=0,link={port2}"]
    proc = subprocess.Popen(args)
    time.sleep(0.5)  # wait for socat to create the ports in the separate process
    yield (port1, port2)

    proc.terminate()
    proc.wait()


@pytest.fixture
def config_port1(socat):
    config = {"port": socat[0], "baudrate": "115200"}
    return config


@pytest.fixture
def config_port2(socat):
    config = {"port": socat[1], "baudrate": "115200"}
    return config


def test_can_instantiate():
    LockInAmplifier(port_settings={})


def test_can_connect_to_port(config_port1):
    lia = LockInAmplifier(port_settings=config_port1)
    trio.run(lia.connect)
    assert lia._ser is not None


@pytest.mark.trio
async def test_can_write_to_port(config_port1):
    lia = LockInAmplifier(port_settings=config_port1)
    await lia.connect()
    lia._ser.reset_input_buffer()
    lia._ser.reset_output_buffer()
    await lia._aser.write(b"foo")


@pytest.mark.trio
async def test_can_read_from_port(config_port1, config_port2):
    dummy_ser = Serial(**config_port2)
    lia = LockInAmplifier(port_settings=config_port1)
    await lia.connect()
    lia._ser.reset_input_buffer()
    lia._ser.reset_output_buffer()
    dummy_ser.write(b"foo")
    msg = await lia._aser.read(3)
    assert msg == b"foo", f"Read {msg}, expected `foo`"


@pytest.mark.trio
async def test_knows_if_connected(config_port1):
    lia = LockInAmplifier(port_settings=config_port1)
    await lia.connect()
    lia._ser.reset_input_buffer()
    lia._ser.reset_output_buffer()
    assert await lia.is_connected()
    lia._ser.close()
    assert not await lia.is_connected()
