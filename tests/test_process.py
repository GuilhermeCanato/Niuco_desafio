from source.probe               import Probe
from source.land                import Land
from source.probe_controller    import ProbeController

import pytest

@pytest.fixture
def land():
    return Land(5, 5)

@pytest.fixture
def probe_controller(land):
    return ProbeController(land)

# Teste para verificar se o processo todo está funcionando como o esperado
def test_all_process(probe_controller):

    probe_controller.add_probe(1, 2, "N", "LMLMLMLMM")
    probe_controller.add_probe(3, 3, "E", "MMRMMRMRRM")
    probe_controller.add_probe(5, 5, "N", "RRMMRM")

    probe_controller.execute_probes()

    result = probe_controller.show_probes_values()

    assert result == [(1, 3, 'N', 'LMLMLMLMM'), (5, 1, 'E', 'MMRMMRMRRM'), (4, 3, 'W', 'RRMMRM')]