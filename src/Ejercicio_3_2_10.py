'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

    Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    Preguntar por el NIF del cliente y mostrar sus datos.
    Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    Terminar el programa.

'''

def pedir_accion():
    '''Pide una opción al usuario por consola

    Return:
        str: opción dada por el usuario 1, 2, 3, 4, 5 o 6
    '''
    accion = None

    while accion == None:
        print('\nElige una opción:\n1. Añadir cliente nuevo a la base de datos\n2. Eliminar un cliente de la base de datos\n3. Mostrar datos de un cliente\n4. Mostrar todos los clientes (NIF y nombre)\n5. Mostrar los clientes preferentes (NIF y nombre)\n6. Terminar y salir del programa')
        accion = input('Opción --> ')

        if accion != '1' and accion != '2' and accion != '3' and accion != '4' and accion != '5' and accion != '6':
            print('**ERROR** - OPCIÓN INCORRECTA')
            accion = None

    return accion


def nuevo_cliente(clientes:dict) -> dict:
    '''Añade un nuevo cliente a la base de datos

    Args:
        clientes (dict): diccionario con los clientes almacenados

    Return:
        dict: diccionario con los clientes actualizado
    '''
    nif = input('NIF: ')
    clientes[nif] = {}

    nombre = input('Nombre: ')
    clientes[nif]['nombre'] = nombre

    direccion = input('Dirección: ')
    clientes[nif]['direccion'] = direccion

    telefono = input('Telefono: ')
    clientes[nif]['telefono'] = telefono

    correo = input('Correo: ')
    clientes[nif]['correo'] = correo

    preferente = input('Preferente (si o no): ')

    while preferente != 'si' and preferente != 'no':
        preferente = input('Preferente (si o no): ')

    if preferente == 'si':
        preferente = True
    else:
        preferente = False

    clientes[nif]['prefentente'] = preferente

    return clientes


def eliminar_cliente(clientes: dict) -> dict:
    '''Pide el NIF del cliente que se quiere eliminar

    Args:
        clientes (dict): diccionario con los clientes almacenados

    Return:
        dict: diccionario con los clientes actualizado
    '''
    nif = input('NIF del cliente que se va a eliminar: ')

    try:
        del clientes[nif]
    except KeyError:
        print('NO EXISTE UN CLIENTE CON EL NIF DADO')

    return clientes


def mostrar_datos(clientes: dict) -> None:
    '''Muestra los datos del cliente que corresponde al NIF dado por el usuario

    Args:
        clientes (dict): diccionario con los clientes almacenados
    '''
    nif = input('NIF del cliente: ')

    if nif in clientes:
        print(clientes[nif])
    else:
        print('NO EXISTE UN CLIENTE CON EL NIF DADO')


def mostrar_todos(clientes: dict) -> None:
    '''Muestra el nif y el nombre de todos los clientes

    Args:
        clientes (dict): diccionario con los clientes almacenados

    Return:
        dict: diccionario con los clientes actualizado
    '''
    for cliente in clientes:
        print(f'NIF: {cliente}\n Nombre: {clientes[cliente]['nombre']}')


def mostrar_preferentes(clientes: dict) -> None:
    '''Muestra el nif y el nombre de todos los clientes prefenrentes

    Args:
        clientes (dict): diccionario con los clientes almacenados

    Return:
        dict: diccionario con los clientes actualizado
    '''
    for cliente in clientes.items():
        if clientes[cliente]['preferente'] == True:
            print(cliente)


def main():
    clientes = {}

    accion = pedir_accion()

    while accion != '6':
        if accion == '1':
            clientes = nuevo_cliente(clientes)
        
        elif accion == '2':
            clientes = eliminar_cliente(clientes)
        
        elif accion == '3':
            mostrar_datos(clientes)
        
        elif accion == '4':
            mostrar_datos(clientes)

        elif accion == '5':
            mostrar_preferentes(clientes)

        accion = pedir_accion()

    print('Cerrando el programa...')


if __name__ == '__main__':
    main()