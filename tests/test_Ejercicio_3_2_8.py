import pytest
from src.Ejercicio_3_2_8 import separar_pares, crear_diccionario, traducir_palabras, traducir_frase

@pytest.mark.parametrize(
    'input_x, expected',
    [
        ('hola:hello,mundo:world,gato:cat', ['hola:hello', 'mundo:world', 'gato:cat']),
        ('casa:house,coche:car,tren:train,arbol:tree', ['casa:house', 'coche:car', 'tren:train', 'arbol:tree']),
        ('yo:i,tengo:am,hambre:hungry', ['yo:i', 'tengo:am', 'hambre:hungry'])
    ]
)

def test_separar_pares_params(input_x, expected):
    assert separar_pares(input_x) == expected


@pytest.mark.parametrize(
    'input_y, expected',
    [
        (['hola:hello', 'mundo:world', 'gato:cat'], {'hola': 'hello', 'mundo': 'world', 'gato': 'cat'}),
        (['casa:house', 'coche:car', 'tren:train', 'arbol:tree'], {'casa': 'house', 'coche': 'car', 'tren': 'train', 'arbol': 'tree'}),
        (['yo:i', 'tengo:am', 'hambre:hungry'], {'yo': 'i', 'tengo': 'am', 'hambre': 'hungry'})
    ]
)

def test_crear_diccionario_params(input_y, expected):
    assert crear_diccionario(input_y) == expected


@pytest.mark.parametrize(
    'input_z, input_a, expected',
    [
        ('Mi gato dice -> hola mundo', {'hola': 'hello', 'mundo': 'world', 'gato': 'cat'}, ['Mi', 'cat', 'dice', '->', 'hello', 'world']),
        ('El tren pasa al lado de la casa del arbol', {'casa': 'house', 'coche': 'car', 'tren': 'train', 'arbol': 'tree'}, ['El', 'train', 'pasa', 'al', 'lado', 'de', 'la', 'house', 'del', 'tree']),
        ('yo tengo mucha hambre' ,{'yo': 'i', 'tengo': 'am', 'hambre': 'hungry'}, ['i', 'am', 'mucha', 'hungry'])
    ]
)

def test_traducir_palabras_params(input_z, input_a, expected):
    assert traducir_palabras(input_z, input_a) == expected


@pytest.mark.parametrize(
    'input_b, expected',
    [
        (['Mi', 'cat', 'dice', '->', 'hello', 'world'], 'Mi cat dice -> hello world'),
        (['El', 'train', 'pasa', 'al', 'lado', 'de', 'la', 'house', 'del', 'tree'], 'El train pasa al lado de la house del tree'),
        (['i', 'am', 'mucha', 'hungry'], 'i am mucha hungry')
    ]
)

def test_traducir_frase_params(input_b, expected):
    assert traducir_frase(input_b) == expected