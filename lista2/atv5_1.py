num1 = int(input('digite o 1 numero: '))
num2 = int(input('digite o 2 numero: '))
num3 = int(input('digite o 3 numero: '))

if num1 > num3 and num1 > num2:
    ma = num1
    if num3 > num2:
        md = num3
        men = num2
    else:
        md = num2
        men = num3
if num2 > num3 and num2 > num1:
    ma = num2
    if num3 > num1:
        md = num3
        men = num1
    else:
        md = num1
        men = num3
if num3 > num2 and num3 > num1:
    ma = num3
    if num2 > num1:
        md = num2
        men = num1
    else:
        md = num1
        men = num2

print(ma)
print(md)
print(men)