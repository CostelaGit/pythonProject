#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
# mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

F = float(input('digite a temperatura em fahrenheit:'))
C = 5 * ((F - 32) / 9)
print('a temperatura em Celsius é:', C)