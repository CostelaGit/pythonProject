"""Faça um Programa que leia três números e mostre o maior deles."""

num1 = float(input('digite numero 1:'))
num2 = float(input('digite numero 2:'))
num3 = float(input('digite numero 3:'))

if num1 > num2 and num1 > num3:
    m_numero = num1
elif num2 > num1 and num2 > num3:
    m_numero = num2
else:
    m_numero = num3

print('maior numero:', m_numero)
