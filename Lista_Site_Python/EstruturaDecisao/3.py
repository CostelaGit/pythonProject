"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

x = input().upper()

if x == 'F':
    print('Sexo Feminino')
elif x == 'M':
    print('Sexo Masculino')
else:
    print('Sexo invalido')