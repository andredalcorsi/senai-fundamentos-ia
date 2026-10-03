'''

025. Leia um número e informe se ele é par ou ímpar.

Dica: o resto da divisão por 2 ( n % 2 ) só pode ser 0 ou 1.

'''

import math

n = int(input("Digite um número: "))

if (n % 2 == 0):
    print('PAR!')
else:
    print('ÍMPAR!')