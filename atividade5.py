alt = float(input('digite a sua altura: '))
sexo = input('digite seu sexo; F - feminino | M - masculino \n')

if sexo == 'F' or 'f':
    alt = (62.1 * alt) - 44.7
    print('seu peso ideal é: ', alt)
elif sexo == 'M' or 'm':
    alt = (72.7 * alt) - 58
    print('seu peso ideal é:', alt)
else:
    print('error')