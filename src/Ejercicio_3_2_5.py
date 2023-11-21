'''
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato '<asignatura> tiene <créditos> créditos', donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
'''

def sumar_creditos(asignaturas: dict) -> int:
    '''Suma los créditos de las asignaturas del diccionario

    Args:
        asignaturas (dict): asignaturas con sus créditos correspondientes

    Return:
        int: suma de los créditos de las asignaturas
    '''
    suma = 0
    for credito in asignaturas:
        suma += asignaturas.get(credito)

    return suma


def main():
    # ENTRADA
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

    # PROCESO
    # pasar las claves a una lista
    nombres = list(asignaturas)
    suma_creditos = sumar_creditos(asignaturas)

    # SALIDA
    for i in range(0, len(asignaturas)):
        print(f'{nombres[i]} tiene {asignaturas.get(nombres[i])} créditos')
    
    print(f'La suma de los créditos es => {suma_creditos}')


if __name__ == '__main__':
    main()