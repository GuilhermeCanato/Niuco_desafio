from source.probe import Probe
from source.land  import Land

import pytest

@pytest.fixture
def land():
    return Land(5, 5)

@pytest.fixture
def probe(land):
    return Probe(1, 3, "N", "LMLMLMLMM", land)

# Testando se ele faz a construção do objeto corretamente
def test_probe_constructor(probe):
    assert probe.x == 1
    assert probe.y == 3
    assert probe.direction == "N"

# Testando se ele segue a sequencia N -> W -> S -> E -> N corretamente
def test_probe_turn_left(probe):
    probe.turn_left()
    assert probe.direction == "W"

    probe.turn_left()
    assert probe.direction == "S"

    probe.turn_left()
    assert probe.direction == "E"

    probe.turn_left()
    assert probe.direction == "N"

# Testando se ele segue a sequencia N -> E -> S -> W -> N corretamente
def test_probe_turn_right(probe):
    probe.turn_right()
    assert probe.direction == "E"

    probe.turn_right()
    assert probe.direction == "S"

    probe.turn_right()
    assert probe.direction == "W"

    probe.turn_right()
    assert probe.direction == "N"

# Testando se o sonda se move corretamente na direção determinada
def test_probe_move(probe):
    # probe = 1, 3, "N"
    probe.move()
    assert probe.y == 4

    probe.move()
    assert probe.y == 5

    probe.turn_right()
    probe.move()
    assert probe.x == 2

    probe.move()
    probe.move()
    assert probe.x == 4

# Testando se o movimento para fora dos limites é ignorado
def test_probe_move(probe):
    # probe = 1, 3, "N"
    probe.move()
    assert probe.y == 4

    probe.move()
    assert probe.y == 5

    # deve continuar no 5
    probe.move()
    assert probe.y == 5

# Testando se a sonda respeita o limite ao girar e tentar mover
def test_probe_rotate_and_move_outside(land):
    probe = Probe(5, 5, "E", "MMM", land)
    probe.move()
    assert probe.x == 5

# Testando se ao criar uma sonda em uma posição ocupada, levanta uma exceção
def test_probe_raises_exception_if_position_occupied(land):
    land.add_position(2, 2)  # Simulando que já existe uma sonda na posição
    with pytest.raises(ValueError):
        Probe(2, 2, "N", "M", land)