b = int(input('digite o ano: '))
if b > 999:
    pass
if (b % 4 == 0 and b % 100 != 0) or b % 400 == 0:
    print('este ano é bissexto')
