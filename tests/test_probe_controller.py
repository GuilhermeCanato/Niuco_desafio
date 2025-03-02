from source.land                import Land
from source.probe               import Probe
from source.probe_controller    import ProbeController

import pytest

@pytest.fixture
def land():
    return Land(5, 5)

@pytest.fixture
def probe_controller(land):
    return ProbeController(land)

def test_pobre_controller(probe_controller):
    probe_controller.add_probe(2, 4, "E", "RRRMMLM")
    probe_controller.add_probe(1, 2, "N", "LMLMLMLMM")

    result = probe_controller.show_probes_values()

    assert result == [(2, 4, 'E', 'RRRMMLM'), (1, 2, 'N', 'LMLMLMLMM')]

