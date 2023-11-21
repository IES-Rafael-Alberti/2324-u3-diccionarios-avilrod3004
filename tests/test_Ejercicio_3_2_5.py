import pytest
from src.Ejercicio_3_2_5 import sumar_creditos

@pytest.mark.parametrize(
    'input_x, expected',
    [
        ({'Matemáticas': 6, 'Física': 4, 'Química': 5}, 15),
        ({'Matemáticas': 7, 'Física': 3, 'Química': 8}, 18),
        ({'Matemáticas': 6, 'Física': 4, 'Química': 5, 'Lengua': 7, 'Historia': 5}, 27),
        ({'Redes Locales': 8, 'Montaje y mantenimiento': 4, 'FOL': 5}, 17)
    ]
)

def test_sumar_creditos_params(input_x, expected):
    assert sumar_creditos(input_x) == expected