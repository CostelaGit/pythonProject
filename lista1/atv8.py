'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido
mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.'''

por_hora = float(input("Digite o quanto você ganha por hora:"))
num_h = float(input("Digite a quantidade de horas trabalhadas no mês: "))
salario_bruto = por_hora * num_h
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
SINDICATO = salario_bruto * 0.05
descontos = IR + INSS + SINDICATO
Salario_liquido = salario_bruto - descontos

print(f'+ Salario bruto: {salario_bruto:.2f}\n'
      f'- IR (11%): {IR:.2f}\n'
      f'- INSS (8%): {INSS:.2f}\n'
      f'- Sindicato (5%): {SINDICATO:.2f}\n'
      f'= Salário Liquido: {Salario_liquido:.2f}')



