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

# Testando se é possível adicionar múltiplas sondas e executá-las corretamente
def test_probe_controller_add_multiple_probes(probe_controller):
    probe_controller.add_probe(1, 2, "N", "LMLMLMLMM")
    probe_controller.add_probe(3, 3, "E", "MMRMMRMRRM")

    probe_controller.execute_probes()
    result = probe_controller.show_probes_values()

    assert result == [(1, 3, "N", "LMLMLMLMM"), (5, 1, "E", "MMRMMRMRRM")]

# Testando se não permite que uma sonda colida com outra
def test_probe_controller_avoid_collision(probe_controller):
    probe_controller.add_probe(1, 2, "N", "M")
    probe_controller.add_probe(1, 1, "N", "MM")  # Essa sonda deveria colidir

    probe_controller.execute_probes()
    result = probe_controller.show_probes_values()

    # Espera-se que a segunda sonda não tenha se movido para evitar colisão
    assert result == [(1, 3, "N", "M"), (1, 2, "N", "MM")]

# Testando se as sondas finalizam no estado correto após a execução dos comandos
def test_probe_controller_final_states(probe_controller):
    probe_controller.add_probe(2, 2, "E", "MM")
    probe_controller.add_probe(3, 3, "N", "MLMR")

    probe_controller.execute_probes()
    result = probe_controller.show_probes_values()

    assert result == [(4, 2, "E", "MM"), (2, 4, "N", "MLMR")]
