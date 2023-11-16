'''
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''
def pedir_divisa() -> str:
    '''Preguntar por la divisa

    Return:
        str: divisa dada por el usuario
    '''
    pregunta = input('Divisa --> ')

    return pregunta


def main():
    divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

    pregunta = pedir_divisa()

    # SALIDA
    if pregunta in divisas:
        print(divisas.get(pregunta))
    else:
        print('**ERROR** - LA DIVISA NO ESTÁ EN EL DICCIONARIO')


if __name__ == "__main__":
    main()