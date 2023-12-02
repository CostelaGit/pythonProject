'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6
metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem
compradas e os respectivos preços em 3 situações:
a. comprar apenas latas de 18 litros;
b. comprar apenas galões de 3,6 litros;
c. misturar latas e galões, de forma que o preço seja o menor.'''

#fatos
# 1 litro a cada 6 metros = area a ser pintada / 6
# latas = 18 litros  | R$ 80.00
# galões = 3.6 litros | R$ 25.00

#1 situação = area / 6 depois passar / 18lt dar resultado em latas
#2 situação = area / 6 depois passar / 3.6lt dar resultado em galoes
#3 situação = area / 6 depois passar em lata, se lata for muito passar para galao e dar resultado de latas e galoes


import math

area_pintar = float(input('digite a area a ser pintada:'))
litro_util = area_pintar / 6

latas_util = math.ceil(litro_util / 18)
preco_latas = latas_util * 80

print('litros utilizados:', litro_util)
print('latas a serem usadas:', latas_util)
print('preco das latas:', preco_latas)



'''very hard'''






"""# Tamanho da área a ser pintada em metros quadrados
area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calculando a quantidade necessária de tinta em litros
cobertura_por_litro = 6
tinta_necessaria = area_a_pintar / cobertura_por_litro

# Comprando apenas latas de 18 litros
latas = math.ceil(tinta_necessaria / 18)
preco_latas = latas * 80

# Comprando apenas galões de 3,6 litros
galoes = math.ceil(tinta_necessaria / 3.6)
preco_galoes = galoes * 25

# Misturando latas e galões para obter o menor preço
latas_misturadas = int(tinta_necessaria // 18)
sobra = tinta_necessaria % 18
galoes_misturados = math.ceil(sobra / 3.6)
preco_misturado = (latas_misturadas * 80) + (galoes_misturados * 25)

# Exibindo os resultados
print(f"a. Comprar apenas latas de 18 litros: {latas} latas por R${preco_latas:.2f}")
print(f"b. Comprar apenas galões de 3,6 litros: {galoes} galões por R${preco_galoes:.2f}")
print(f"c. Misturar latas e galões: {latas_misturadas} latas e {galoes_misturados} galões por R${preco_misturado:.2f}")"""

