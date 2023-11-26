import pytest
from src.Ejercicio_3_2_3 import calcular_precio

@pytest.mark.parametrize(
    'input_x, input_y, expected',
    [
        (1.35, 2.5, 3.375),
        (0.80, 1.2, 0.96),
        (0.85, 0.5, 0.425),
        (0.70, 2.5, 1.75)
    ]
)

def test_calcular_precio_params(input_x, input_y, expected):
    assert calcular_precio(input_x, input_y) == expected