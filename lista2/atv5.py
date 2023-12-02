'''5. Faça um Programa que leia três números e mostre-os em ordem decrescente. Usando apenas:
o If e else
o If, else e operadores lógicos
o If e elif'''

num1 = int(input('digite o 1 numero: '))
num2 = int(input('digite o 2 numero: '))
num3 = int(input('digite o 3 numero: '))

ma = None
md = None
men = None

if num1 > num2:
    if num1 > num3:
        ma = num1
        if num2 > num3:
            md = num2
            men = num3
        else:
            md = num3
            men = num2
if num2 > num1:
    if num2 > num3:
        ma = num2
        if num1 > num3:
            md = num1
            men = num3
        else:
            md = num3
            men = num1
if num3 > num1:
    if num3 > num2:
        ma = num3
        if num1 < num2:
            md = num2
            men = num1
        else:
            md = num1
            men = num2

print(ma)
print(md)
print(men)