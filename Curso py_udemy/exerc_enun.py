x = int(input('digite um numero inteiro:'))

if x % 2 == 0:
    print('esse numero é par')
else:
    print('este numero é impar')

#################################################

hora = int(input('digite a hora:'))
if hora >= 0 and hora <= 11:
    print('Bom dia')
elif hora >= 12 and hora <= 17:
    print('Boa Tarde')
elif hora >= 18 and hora <= 23:
    print('Boa Noite')

#################################

nome = input('digite o seu nome:')
if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) == 5 or len(nome) == 6:
    print('Seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é muito grande')