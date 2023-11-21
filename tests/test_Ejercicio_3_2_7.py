import pytest
from src.Ejercicio_3_2_7 import calcular_coste

@pytest.mark.parametrize(
    'input_x, expected',
    [
        ({'tomates': 0.5, 'lechuga': 1.2, 'lentejas': 0.7, 'helados': 0.6}, 3),
        ({'macarrones': 0.6, 'tomates': 0.5, 'pate': 1.4, 'pimienta': 0.3}, 2.8),
        ({'mortadela': 0.4, 'pan de model': 1.3, 'garbanzos': 0.5}, 2.2),
        ({'jamon': 1.5, 'lechuga': 0.6, 'champu': 2.6}, 4.7)
    ]
)

def test_calcular_coste_params(input_x, expected):
    assert calcular_coste(input_x) == expected
