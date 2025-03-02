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