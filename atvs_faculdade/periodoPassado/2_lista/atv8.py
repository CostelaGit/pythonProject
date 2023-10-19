salario = float(input('digite o seu salario: '))

if salario < 280:
    tx = 0.2
    aum = salario * tx
    salarionv = salario + aum
elif salario >= 280 and salario < 700:
    tx = 0.15
    aum = salario * tx
    salarionv = salario + aum
elif salario >= 700 and salario < 1500:
    tx = 0.10
    aum = salario * tx
    salarionv = salario + aum
elif salario >= 1500:
    tx = 0.05
    aum = salario * tx
    salarionv = salario + aum
else:
    print('digite apenas numeros')

print('salario antes do reajuste:', salario, '\ntaxa aplicada:', tx,
      '\naumento:', aum, '\nnovo salario apos o aumento:', salarionv)
