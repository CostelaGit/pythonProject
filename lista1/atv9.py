'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa
que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante: aumento de 5%
Após o aumento ser realizado, informe na tela:
a. o salário antes do reajuste;
b. o percentual de aumento aplicado;
c. o valor do aumento;
d. o novo salário, após o aumento.'''

print("Organizações Tabajara - Reajuste de salario\n")
salario = float(input('\ndigite o seu salário:'))

p = None
v = None
s_aumento = None

if salario <= 280:
  p = float(0.2)
  v = salario * p
  s_aumento = salario + v
  p = '20%'
elif 280 < salario < 700:
  p = float(0.15)
  v = salario * p
  s_aumento = salario + v
elif 700 < salario < 1500:
  p = float(0.10)
  v = salario * p
  s_aumento = salario + v
elif salario > 1500:
  p = float(0.05)
  v = salario * p
  s_aumento = salario + v
else:
  print('error')

print('\nsalario antes do reajuste: R$ ', salario)
print('\npercentual de aumento aplicado ao salario:', p)
print('\nvalor do aumento: R$ %.2f ' % v)
print('\nnovo salário, após o aumento: R$', s_aumento)