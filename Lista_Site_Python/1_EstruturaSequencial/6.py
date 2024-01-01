#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# calculo do circulo = area do circulo = pi*raio**2
#aqui começa já caso queira ser mais preciso, importar a biblioteca math
pi = 3.14
x = float(input('digite o tamanho do raio: '))

x = pi * (x ** 2)

print('o tamanho do circulo é:', x)