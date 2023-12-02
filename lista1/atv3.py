''' Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a
temperatura em graus Celsius. C = (5 * (F-32) / 9).'''


graus_f = float(input("digite a temperatura em graus Fahrenheit: "))
graus_c = (5 * (graus_f - 32) / 9)
print("a temperatura transformada em graus Celsius: ", graus_c)