a = float(input('digite um numero:'))
b = float(input('digite um segundo numero:'))
c = float(input('digite um terceiro numero:'))

if a > b and a > c:
    mn = a
    if b > c:
        md = b
        min = c
    else:
        md = c
        min = b
elif b > a and b > c:
    mn = b
    if a > c:
        md = a
        min = c
    else:
        md = c
        min = a
elif c > a and c > b:
    mn = c
    if a > b:
        md = a
        min = b
    else:
        md = b
        min = a

print(min, md, mn)
