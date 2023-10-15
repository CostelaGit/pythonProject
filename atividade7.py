peso = float(input('digite o peso dos peixes'))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print('o peso excedente:', excesso,'\n','a multa é de:', multa)
else:
    print('dentro do regulamento, sem pagamento de multa.')