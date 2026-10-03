'''

031 - Leia um ano e informe se ele é bissexto: divisível por 4, exceto se for divisível por 100 e não por
400.

Dica: a regra inteira cabe em uma expressão só com and , or e parênteses.

'''

ano = int(input('Digite um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é BISSEXTO!')
else:
    print(f'{ano} NÃO É BISSEXTO!')