"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

x = float(input('digite o tamanho a ser pintada:'))

cobertura = 6
latas = 18
galao = 3.6
v_lata = 80
v_galao = 25


# situaçao 1
litros_ne = x / cobertura
latas_n = litros_ne / latas
v_lata_total = latas_n * v_lata
print('situação 1 - Só latas de 18 litros:', int(latas_n))

# Situação 2
litros_ne_g = x / cobertura
galao_n = litros_ne_g / galao
v_galao_total = galao_n * v_galao
print('situação 2 - Só galao de 3.6 litros:', int(galao_n))

# aqui pra cima eu conseguir utilizando a atv anterior


# Situação 3

## AQUI É FULL GPT pq eu não entendia como fazer

litros_ne_lg = (x / cobertura) * 1.1
qtd_l = int(litros_ne_lg / latas)
qtd_g = int(litros_ne_lg / galao)
preco_t_l = qtd_l * v_lata
preco_t_g = qtd_g * v_galao

combinacao_economica = None
menor_preco = float('inf')

for num_latas in range(int(litros_ne_lg / latas) + 1):
    litros_restantes = litros_ne_lg - (num_latas * latas)
    num_galoes = int(litros_restantes / galao)
    preco_t_lg = (num_latas * preco_t_l) + (num_galoes * preco_t_g)

    if preco_t_lg < menor_preco:
        menor_preco = preco_t_lg
        combinacao_economica = (num_latas, num_galoes)

num_latas, num_galoes = combinacao_economica
print('situação 3 - misturando galoes e latas:')
print('quantidade de latas de tintas:', num_latas)
print('quantidade de galoes de tintas', num_galoes)
print('preco total a ser pago R$:', menor_preco)