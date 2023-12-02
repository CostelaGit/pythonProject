'''if else e operadores logicos'''

letra = input('digite uma letra: ').lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} não é uma vogal')