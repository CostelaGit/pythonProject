'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''


num1 = float(input('digite numero 1:'))
num2 = float(input('digite numero 2:'))
num3 = float(input('digite numero 3:'))

if num1 > num2 and num1 > num3:
    m_numero = num1
    if num2 > num3:
        menor_num = num3
    else:
        menor_num = num2
elif num2 > num1 and num2 > num3:
    m_numero = num2
    if num1 > num3:
        m_numero = num3
    else:
        m_numero = num1
else:
    m_numero = num3
    if num2 > num1:
        menor_num = num1
    else:
        menor_num = num2

print('maior numero:', m_numero)
print('menor numero:', menor_num)