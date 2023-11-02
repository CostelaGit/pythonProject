"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

x = int(input('numero inteiro:'))
y = int(input('numero inteiro:'))
w = float(input('numero real: '))

print('a.', (2 * x)*(y / 2))
print('b.', (x*3)+w)
print('c.', w**3)