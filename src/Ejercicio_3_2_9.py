'''
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
'''

def pedir_accion() -> str:
    '''Pide una opción al usuario por consola

    Return:
        str: opción dada por el usuario 1, 2, o 3
    '''
    accion = None

    while accion == None:
        print('\nElige una opción:\n1. Añadir una nueva factura\n2. Pagar una factura existente\n3. Terminar y salir del programa')
        accion = input('Opción --> ')

        if accion != '1' and accion != '2' and accion != '3':
            print('**ERROR** - OPCIÓN INCORRECTA')
            accion = None

    return accion


def nueva_factura(facturas: dict, pendiente: float) -> dict:
    '''Pide al usuario el número de la factura nueva y su coste

    Args:
        facturas (dict): todas las facturas pendientes
        pendiente (float): suma de las facturas pendiente de pagar

    Retunr:
        dict: facturas pendientes actualizadas
        float: suma de las facturas pendientes por pagar actualizado
    '''
    num_factura = input('Introduce el número de la factura: ')
    coste = float(input('Introduce el coste de la factura: '))

    facturas[num_factura] = coste
    pendiente += facturas.get(num_factura)

    return facturas, pendiente


def pagar_factura(facturas: dict, cobrado: float, pendiente: float) -> dict:
    '''Pide al usuario el número de la factura que quiere pagar y la elimian las facturas pendientes

    Args:
        facturas (dict): facturas pendientes
        cobrado (float): suma de facturas pagadas
        pediente (float): suma de las facturas pendiente de pagar

    Retunr:
        dict: facturas pendientes actualizadas
        float: suma de las facturas pagadas actualizado
        float: suma de las facturas pendiente por pagar actualizado
    '''
    num_factura = input('Introduce el número de la factura: ')

    if num_factura in facturas:
        cobrado += facturas.get(num_factura)
        pendiente -= facturas.get(num_factura)
        del facturas[num_factura]

    else:
        print('\nNO EXISTE UNA FACTURA CON ESE NÚMERO')

    return facturas, cobrado, pendiente


def main():
    facturas = {}
    cobrado = 0
    pendiente = 0

    print('\nPROGRAMA PARA LA GESTIÓN DE FACTURAS PENDIENTES DE COBRO')

    # ENTRADA
    accion = pedir_accion()

    while accion != '3':

        if accion == '1':
            facturas, pendiente = nueva_factura(facturas, pendiente)

        # PROCESO
        elif accion == '2':
            facturas, cobrado, pendiente = pagar_factura(facturas, cobrado, pendiente)

        # SALIDA
        print(f'\nCobrado hasta el momento: {cobrado}€\nPendiente de cobro: {pendiente}€')
        accion = pedir_accion()

    print('Cerrando el programa...')


if __name__ == '__main__':
    main()