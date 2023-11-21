'''
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra 	
Artículo 1 	    Precio
Artículo 2 	    Precio
Artículo 3 	    Precio
… 	            …
Total 	        Coste
'''

def pedir_opcion() -> int:
    '''Pregunta al usuario si quiere introducir un articulo en la lista de la compra o terminar y mostrar la lista

    Return:
        int: opción elegida por el usuario
    '''
    opciones = ['1', '2', '3']
    opcion = ''

    while opcion not in opciones:
        opcion = input('\n ELIGE UNA OPCIÓN:\n 1. Añadir artículo a la lista\n 2. Terminar y mostrar lista\n --> ')

    return opcion


def pedir_articulo() -> str:
    '''Pide un articulo al usuario por consola

    Return:
        str: articulo dado por el usuario
    '''
    articulo = input('\nArticulo --> ')

    while articulo.isdecimal() == True:
        print('**ERROR**')
        articulo = input('\nArticulo --> ')

    return articulo


def pedir_precio() -> float:
    '''Pide el precio del articulo añadido

    Retunr:
        float: precio del artículo
    '''
    formato = False

    while formato == False:
        try:
            precio = float(input('Precio --> '))
        except ValueError:
            print('**ERROR** - FORMATO DEL PRECIO INCORRECTO')
        except:
            print('**ERROR**')
        else:
            formato = True

    return precio


def calcular_coste(lista_compra: dict) -> float:
    '''Suma el precio de los artículos

    Args:
        lista_compra (dict): diccionario con los artículos y sus precios

    Return:
        float: suma de los precios
    '''
    suma = 0
    for articulo in lista_compra:
        suma += lista_compra[articulo]

    return suma


def mostrar_lista(lista_articulos: list, lista_compra: dict, coste: float) -> str:
    '''
    
    Args:
        lista_articulos (list): lista con los articulos (claves) del diccionario
        lista_compra (dict): diccionario con los articulos y sus precios
        coste (float): suma de los precios de todos los artículos
    '''
    imprimir_lista = '\n LISTA DE LA COMPRA\n'

    for i in range(0, len(lista_articulos)):
        imprimir_lista += f'{lista_articulos[i]}         {lista_compra.get(lista_articulos[i])}\n'

    imprimir_lista += f'Total           {coste}'

    return imprimir_lista


def main():
    lista_compra= {}
    opcion = '1'
    print('\nLISTA DE LA COMPRA:\nAñade todos los artículos que quieras\n')

    while opcion == '1':
        # ENTRADA
        articulo = pedir_articulo()
        precio = pedir_precio()
        
        # PROCESO
        # guardar los articulos como clave y el precio como valor en el diccionario
        lista_compra[articulo] = precio
        
        opcion = pedir_opcion()

    # SALIDA
    if opcion == '2':
        coste = calcular_coste(lista_compra)
        print(mostrar_lista(list(lista_compra), lista_compra, coste))


if __name__ == '__main__':
    main()