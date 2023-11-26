'''
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
'''
def pedir_palabras() -> str:
    '''Pide al usuario por consola palabras en español y en inglés para hacer un diccionario

    Return:
        str: palabras dadas por el usuario
    '''
    print('\nIntroduce las palabras siguiendo este ejemplo: \npalabra_español:palabra_ingles,palabra_español1...')
    palabras = input('\n> ')

    return palabras


def pedir_frase() -> str:
    '''Pide una frase al usuario para traducirla

    Return:
        str: frase dada por el usuario
    '''
    frase = input('\nIntroduce la frase que quieres traducir: ')

    return frase


def separar_pares(palabras: str) -> list:
    '''Separa las parejas de las palabras en español e inglés

    Return:
        list: lista con las parejas de palabras
    '''
    lista_pares = palabras.split(',')

    return lista_pares


def crear_diccionario(lista_pares: list) -> dict:
    '''Crear un diccionario, la palabra en español será la clave y la palabra en inglés será el valor

    Args:
        lista_pares (list): lista con las parejas de las palabras en español e inglés

    Return:
        dict: diccionario español-inglés
    '''
    diccionario = {}
    for i in range(0, len(lista_pares)):
        par = lista_pares[i] # toma el valor de la posición i de la lista
        par = par.split(':') # crea una lista con la palabra en español y la palabra en inglés de la posición i de la lista
        diccionario[par[0]] = par[1] # la palabra en español será la clave y la palabra en inglés será el valor

        i += 1

    return diccionario


def traducir_palabras(frase: str, diccionario: dict) -> list:
    '''Compruba las palabras si las palabras de la frase están en el diccionario. Si está la cambia por la palabra en inglés del diccionario

    Args:
        frase (str): frase dada por el usuario para traducirla a inglés
        diccionario (dict): diccionario con las palabras en español e inglés

    Return:
        list: lista con las palabras de la frase. Si estaban en el diccionario están en inglés
    '''
    lista_frase = frase.split(' ')

    for i in range(0, len(lista_frase)):
        palabra = lista_frase[i]

        if palabra in diccionario:
            lista_frase[i] = diccionario.get(palabra)

        i += 1

    return lista_frase


def traducir_frase(palabras_traducidas: list) -> str:
    '''Añade las palabras traducidas o no a una cadena de texto

    Args:
        palabras_traducidas (list): palabras de la frase, si estaban en el diccionario están en inglés

    Return:
        str: traducción de la frase dada por el usuario
    '''
    frase = ''

    for i in range(0, len(palabras_traducidas)):
        if i == 0:
            frase += palabras_traducidas[i]
        else:
            frase += f' {palabras_traducidas[i]}'

        i += 1

    return frase


def main():
    # ENTRADA
    palabras = pedir_palabras()

    # PROCESO
    # separar los conjuntos de palabras en español e inglés
    lista_pares = separar_pares(palabras)
    # crear un diccionario, la clave la palabra en español y el valor la palabra en inglés
    diccionario = crear_diccionario(lista_pares)

    # ENTRADA
    frase = pedir_frase()

    # PROCESADO
    palabras_traducidas = traducir_palabras(frase, diccionario)

    # SALIDA
    print(f'\nFRASE TRADUCIDA => {traducir_frase(palabras_traducidas)}')
    

if __name__ == '__main__':
    main()