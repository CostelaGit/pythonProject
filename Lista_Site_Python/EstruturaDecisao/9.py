'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

num1 = float(input('digite um numero1:'))
num2 = float(input('digite um numero2:'))
num3 = float(input('digite um numero3:'))

if num1 > num2 and num1 > num3:
    m_num = num1
    if num2 > num3:
        medio_num = num2
        menor_num = num3
    else:
        medio_num = num3
        menor_num = num2
elif num2 > num1 and num2 > num3:
    m_num = num2
    if num1 > num3:
        medio_num = num1
        menor_num = num3
    else:
        medio_num = num3
        menor_num = num1
else:
    m_num = num3
    if num1 > num2:
        medio_num = num1
        menor_num = num2
    else:
        medio_num = num2
        menor_num = num1

print(m_num,medio_num,menor_num)