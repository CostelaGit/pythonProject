"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""

gh = float(input('digite o quanto você ganha por hora:'))
ht = float(input('digite a quantidade de horas trabalhadas:'))

salario_bruto = gh * ht
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
Sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (IR + INSS + Sindicato)

print('+ Salaario Bruto: R$', salario_bruto)
print('- IR: R$', IR)
print('- INSS: R$', INSS)
print('- Sindicato: R$', Sindicato)
print('= Salario Liquido: R$', salario_liquido)