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

# Testa o funcionamento da classe ProbeController
def test_pobre_controller(probe_controller):
    probe_controller.add_probe(2, 4, "E", "RRRMMLM")
    probe_controller.add_probe(1, 2, "N", "LMLMLMLMM")

    result = probe_controller.show_probes_values()

    assert result == [(2, 4, 'E', 'RRRMMLM'), (1, 2, 'N', 'LMLMLMLMM')]

# Testando se levanta uma exceção se criar uma sonda fora dos limites
def test_out_limits(probe_controller):
    with pytest.raises(ValueError):
        probe_controller.add_probe(7, 7, "N", "MMRRM")

