'''Faça um programa que pergunte o preço de três produtos e
informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''

p1 = float(input('digite preço do p1:'))
p2 = float(input('digite preço do p2:'))
p3 = float(input('digite preço do p3:'))

if p1 > p2 and p1 > p3:
    if p2 > p3:
        menor_ = p3
    else:
        menor_ = p2
else:
    menor_ = p1

if p2 > p1 and p2 > p3:
    if p3 > p1:
        menor_ = p1
    else:
        menor_ = p3
else:
    menor_ = p2

if p3 > p1 and p3 > p2:
    if p2 > p1:
        menor_ = p1
    else:
        menor_ = p2
else:
    menor_ = p3

print('menor preço:', menor_)