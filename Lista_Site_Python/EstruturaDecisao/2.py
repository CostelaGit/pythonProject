'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

x = float(input('digite um numero'))

if x > 0:
    print('o valor é positivo')
elif x == 0:
    print('valor nulo')
else:
    print('o valor é negativo')