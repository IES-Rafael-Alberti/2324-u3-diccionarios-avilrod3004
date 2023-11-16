'''
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta 	           Precio
Plátano 	        1.35
Manzana 	        0.80
Pera 	            0.85
Naranja 	        0.70

'''

def pedir_fruta(msj, precios: dict) -> str:
    '''Pide una fruta y comprueba si está en la lista

    Args:
        msj: mensaje que se mostrará por pantalla
        precios (dict): diccionario con las frutas y sus precios

    Return:
        str(str): fruta dada por el usuario
    '''
    fruta = input(msj).lower()

    while fruta not in precios:
        print('**ERROR** - LA FRUTA NO ESTÁ EN LA LISTA')
        fruta = input(msj)

    return fruta



def pedir_kilos(kilos):
    '''Pide los kilos que se quieren comprar de la fruta

    Args:
        msj (str): mensaje que se mostrará por pantalla

    Return:
        float: número de kilos 
    '''
    kilos = None

    while kilos == None:
        kilos = input('¿Cuántos kilos? ')

        try:
            kilos = float(kilos)
        except ValueError:
            print('**ERROR** - EL VALOR INTRODUCIDO NO ES UN NÚMERO')
    return kilos


def calcular_precio(precio: float, kilos: float) -> float:
    '''Calcular el precio dependiendo de la fruta que se quiera comprar y de su precio por kilo

    Args:
        precio (float): precio por kilo
        kilos (float): kilos que quiere comprar el usuario

    Retunr:
        float: precio
    '''
    precio = kilos * precio

    return precio


def main():
    frutas = {'platano': 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.70}

    # ENTRADA
    fruta = pedir_fruta('¿Qué fruta quieres comprar? ', frutas)
    kilos = pedir_kilos(kilos)

    # PROCESO
    precio = calcular_precio(frutas.get(fruta), kilos)

    # SALIDA
    print(f'El precio de {kilos}kg de {fruta}s es {precio:.2f}€')



if __name__ == '__main__':
    main()