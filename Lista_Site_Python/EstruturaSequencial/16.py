"""Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao
usuário a quantidades de latas de tinta a serem compradas e o preço total."""

#tive que usar chatgpt pra entender a pergunta... talvez esteja precisando reforçar matematica!!!


area_p = float(input('digite a area a ser pintada:'))

cobertura = 3
tamanho_l = 18
preco_l = 80

litros_ne = area_p / cobertura
qtd_l = litros_ne / tamanho_l
preco_l_t = qtd_l * preco_l

print('vai ser necessario:', litros_ne)
print('qtd de latas:', qtd_l)
print('preco total:', preco_l_t)