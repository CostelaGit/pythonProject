num1 = float(input('digite um numero'))
num2 = float(input('digite o segundo numero'))
num3 = float(input('digite um terceiro numero'))

if num1 > num2 and num1 > num3:
    ma = num1
    if num2 > num3:
        mn = num3
    else:
        mn = num2
elif num2 > num1 and num2 > num3:
    ma = num2
    if num1 > num3:
        mn = num3
    else:
        mn = num1
elif num3 > num1 and num3 > num2:
    ma = num3
    if num1 > num2:
        mn = num2
    else:
        mn = num1
else:
    print('lascou tudo....')

print('\nmaior numero:', ma, '\nmenor numero:', mn)
