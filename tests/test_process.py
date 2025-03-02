from source.probe import Probe
from source.land  import Land

import pytest

@pytest.fixture
def land():
    return Land(5, 5)

@pytest.fixture
def probe(land):
    return Probe(3, 3, "E", land)

def test_all_process(probe):
    probe.execute_comands("MMRMMRMRRM")

    assert probe.x == 5
    assert probe.y == 1
    assert probe.direction == "E"