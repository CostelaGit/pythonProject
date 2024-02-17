salario_c = float(input('digite o salario do colaborador: '))
salario_ar = salario_c
salario_n = None
perc_au = None
valor_au = None

if salario_c <= 280:
    perc_au = 0.2
    salario_n = salario_c + (salario_c * perc_au)
    valor_au = salario_n - salario_c
    print(f'salario antes do reajuste:{salario_ar}\n'
          f'percentual de aumento aplicado: {perc_au}\n'
          f'valor de aumento: {valor_au}\n'
          f'Novo salario, após o aumento: {salario_n}\n')
elif salario_c > 280 or salario_c < 700:
    perc_au = 0.15
    salario_n = salario_c + (salario_c * perc_au)
    valor_au = salario_n - salario_c
    print(f'salario antes do reajuste:{salario_ar}\n'
          f'percentual de aumento aplicado: {perc_au}\n'
          f'valor de aumento: {valor_au}\n'
          f'Novo salario, após o aumento: {salario_n}\n')
elif salario_c > 700 or salario_c < 1500:
    perc_au = 0.10
    salario_n = salario_c + (salario_c * perc_au)
    valor_au = salario_n - salario_c
    print(f'salario antes do reajuste:{salario_ar}\n'
          f'percentual de aumento aplicado: {perc_au}\n'
          f'valor de aumento: {valor_au}\n'
          f'Novo salario, após o aumento: {salario_n}\n')
elif salario_c > 1500:
    perc_au = 0.5
    salario_n = salario_c + (salario_c * perc_au)
    valor_au = salario_n - salario_c
    print(f'salario antes do reajuste:{salario_ar}\n'
          f'percentual de aumento aplicado: {perc_au}\n'
          f'valor de aumento: {valor_au}\n'
          f'Novo salario, após o aumento: {salario_n}\n')
else:
    print('Erro, Nao deveria estar aqui!')