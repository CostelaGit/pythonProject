'''Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo inválido.'''

letra = input('Digite M - Masculino e F - Feminino:' ).upper()

if letra == 'M':
    print('Masculino')
elif letra == 'F':
    print('Feminino')
else:
    print('Sexo inválido')
