''' Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os
valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno.'''

# Solicitando os lados do triângulo
lado1 = float(input("Digite o tamanho do primeiro lado do triângulo: "))
lado2 = float(input("Digite o tamanho do segundo lado do triângulo: "))
lado3 = float(input("Digite o tamanho do terceiro lado do triângulo: "))

# Verificando se os lados formam um triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Verificando o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("Os lados informados formam um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os lados informados formam um triângulo isósceles.")
    else:
        print("Os lados informados formam um triângulo escaleno.")
else:
    print("Os lados informados não formam um triângulo.")

'''hard'''