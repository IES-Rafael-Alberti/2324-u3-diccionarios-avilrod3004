'''
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
'''

def pedir_datos(msj: str) -> str:
    '''Pide información al usuario por consola

    Args:
        msj (str): mensaje que mostrará por pantalla

    Return:
        str: cadena de texto dada por el usuario
    '''
    dato = input(msj)

    return dato

def main():
    datos = {'nombre': '', 'edad': '', 'sexo': '', 'tlf': '', 'correo': '', 'direccion': ''}

    # ENTRADA y PROCESO
    for dato in datos:
        datos[dato] = pedir_datos(f'{dato}: ')

        # SALIDA
        print(datos)


if __name__ == '__main__':
    main()