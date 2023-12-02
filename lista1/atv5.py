'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo.
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.'''

num_1 = int(input("digite o primeiro numero inteiro: "))
num_2 = int(input("digite o segundo numero inteiro: "))
num_3 = float(input("digite o terceiro numero real: "))

q1 = (num_1 * 2) * (num_2 / 2)
q2 = (num_1 * 3) + (num_3 * 3)
q3 = num_3**3
print("resposta da primeira questão: ", q1)
print("resposta da segunda questão: ", q2)
print("resposta da terceira questão: ", q3)