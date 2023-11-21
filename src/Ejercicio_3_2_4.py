'''
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato "dd de <mes> de aaaa" donde <mes> es el nombre del mes.
'''

def pedir_fecha() -> list:
    '''Pide una fecha al usuario por consola y comprueba que tenga el formato correcto

    Return:
     list: fecha dada por el usuario
    '''
    formato = False
    while formato == False:
        fecha = input('Introduce una fecha (dd/mm/aaaa): ')
        fecha = fecha.split('/')

        if len(fecha) == 3:

            decimal = 0

            for i in fecha:
                if i.isdecimal() == True:
                    decimal += 1
            
            if decimal == 3:
                formato = True
            else:
               print('**ERROR** - FORMATO DE FECHA INCORRECTO')

        else:
            print('**ERROR** - FORMATO DE FECHA INCORRECTO')

    return fecha


def main():
    meses = {'01': 'enero', '02': 'febrero', '03': 'marzo', '04': 'abril', '05': 'mayo', '06': 'junio', '07': 'julio', '08': 'agosto', '09': 'septiembre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'}
    
    #ENTRADA
    fecha = pedir_fecha()

    # SALIDA
    print(f'{fecha[0]} de {meses.get(fecha[1])} de {fecha[2]}')


if __name__ == '__main__':
    main()