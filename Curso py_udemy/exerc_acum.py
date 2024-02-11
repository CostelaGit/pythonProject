nome = input('digite seu nome:')
idade = input('digite sua idade')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:                             # visualizar Solução
        print('seu nome contem espaços')
    else:
        print('seu nome NÃO contem espaços')
    print(f'Seu nome tem {len(nome)} letras')    # visualizar solução
    print(f'A primeira letra do seu nome é {nome[:1:]}')
    print(f'A ultima letra do seu nome é {nome[-1::]}')

'''if nome == '' and idade == '':
    print('Desculpa, você deixou campos vazios!')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    """if '' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')"""
    #print('Seu nome contem %d' % (nome.len))
    print(f'A primeira letra do seu nome é {nome[:1:]}')
    print(f'A ultima letra do seu nome é {nome[-1::]}')'''