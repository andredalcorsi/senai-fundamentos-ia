'''
9. Leia três medidas e informe se elas podem formar um triângulo. Cada lado deve ser menor que
a soma dos outros dois.
'''

l1 = int(input('Digite o 1º lado do triângulo: '))
l2 = int(input('Digite o 2º lado do triângulo: '))
l3 = int(input('Digite o 3º lado do triângulo: '))

if (l1 < (l2 + l3)) and (l2 < (l1 + l3)) and (l3 < (l1 + l2)):
    print('É UM TRIÂNGULO!')
else:
    print('NÃO É UM TRIÂNGULO!')