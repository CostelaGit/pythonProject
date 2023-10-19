n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

md = (n1 + n2) / 2

if md >= 7:
    if md == 10:
        print('aprovado com distinção')
    else:
        print('aprovado')
else:
    print('reprovado')
