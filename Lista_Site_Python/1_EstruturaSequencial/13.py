"""Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

h = float(input('digite a altura:'))
sexo = input('digite seu Sexo | F- Feminino ou M- Masculino: ').lower()

if sexo == 'm':
    peso_I = (72.7 * h) - 58
    print('seu peso ideal | Homem:', peso_I)
elif sexo == 'f':
    peso_I = (62.1*h) - 44.7
    print('seu peso ideal | Mulher:', peso_I)
else:
    print('digite os caracteres dentre os 2 sexos')
