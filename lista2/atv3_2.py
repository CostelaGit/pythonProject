'''if elif'''

ano = int(input('digite o ano: '))
verdade = None

if ano % 4 == 0:
    verdade = True
    if ano % 100 != 0:
        verdade = False
        if ano % 400 == 0:
            verdade = True

elif verdade == True:
    print('ano é bissexto')
elif verdade == False:
    print('ano não é bissexto')


'''if ano % 4 == 0:
    verdade = True
    print('ano é bissexto')
    if ano % 100 != 0:
        verdade = None
        if ano % 400 == 0:
            verdade = True
            print('ano é bissexto')
        elif verdade == None:
            print('não é bissexto')
    elif verdade == True:
        print('ano é bissexto')
elif verdade == None:
    print('não é bissexto')'''
