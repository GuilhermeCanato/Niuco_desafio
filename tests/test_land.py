from source.land import Land

import pytest

@pytest.fixture
def land():
    return Land(5, 5)

# Testando se ele faz a construção do objeto corretamente
def test_land_constructor(land):
    assert land.height == 5
    assert land.width == 5

# Testando se o retorno da função 'inside_limits' retorna corretamente o bool True/False
def test_land_limits(land):
    assert land.inside_limits(4, 4) == True
    assert land.inside_limits(10, 7) == False
    assert land.inside_limits(4, 8) == False
    assert land.inside_limits(0, 0) == True

# Testando se adiciona uma posição corretamente no planalto/terreno
def test_land_add_position(land):
    land.add_position(2, 2)
    assert (2, 2) in land.probe_positions

# Testando se não permite adicionar uma posição já ocupada
def test_land_check_free_position(land):
    land.add_position(2, 2)
    assert land.check_position(2, 2) == False  # Deve indicar que está ocupada
    assert land.check_position(3, 3) == True  # Deve indicar que está livre