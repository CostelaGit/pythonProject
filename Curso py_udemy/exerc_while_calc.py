while True:
    numero_1 = input('digite um numero: ')
    numero_2 = input('digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')

    if numero_1.isdigit() and numero_2.isdigit():
        if operador == '+':
            resultado = int(numero_1) + int(numero_2)
            print(resultado)
        elif operador == '-':
            resultado = int(numero_1) - int(numero_2)
            print(resultado)
        elif operador == '/':
            resultado = int(numero_1) / int(numero_2)
            print(resultado)
        elif operador == '*':
            resultado = int(numero_1) * int(numero_2)
            print(resultado)
        else:
            print('operador não reconhecido')
    #########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break
