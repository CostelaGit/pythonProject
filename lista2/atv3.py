'''Faça um Programa que peça para entrar com um ano com 4 dígitos e determine se o mesmo é ou não
bissexto. Obs.: identificar as regras para um ano ser ou não bissexto na internet.
Faça três versões usando apenas:
-if else
-if else e operadores logicos
-if elif'''

ano = int(input("Digite um ano com 4 dígitos: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")
    else:
        print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
