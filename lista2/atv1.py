'''Faça um Programa que peça dois números e imprima o maior deles.'''

num1 = None
num2 = None

num1 = float(input('digite o numero 1: '))
num2 = float(input('digite o numero 2: '))

if num1 > num2:
    MA = num1
else:
    MA = num2

print(MA)