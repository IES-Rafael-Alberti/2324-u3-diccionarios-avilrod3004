'''
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
'''

def pedir_datos(msj) -> str:
    '''Input para pedir un str por consola al usuario

    Args:
        msj: mensaje del input

    Return:
        str: respuesta del usuario
    '''
    dato = input(msj)

    return dato

def main():
    datos = {'nombre': '', 'edad': '', 'direccion': '', 'telefono': ''}

    # ENTRADA
    nombre = pedir_datos('Introduce tu nombre: ')
    edad = pedir_datos('Introduce tu edad: ')
    direccion = pedir_datos('Introduce tu direccion: ')
    telefono = pedir_datos('Introduce tu teléfono: ')


    # PROCESO
    # asigna a cada clave del diccionario la informacion correspondiente del usuario
    datos['nombre'] = nombre
    datos['edad'] = edad
    datos['direccion'] = direccion
    datos['telefono'] = telefono


    # SALIDA
    print(f'{datos.get('nombre')} tiene {datos.get('edad')} años, vive en {datos.get('direccion')} y su número de teléfono es {datos.get('telefono')}')


if __name__ == '__main__':
    main()