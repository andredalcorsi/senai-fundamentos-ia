'''

028 - Leia três números e mostre qual é o maior, sem usar a função max() .

'''

n1 = int(input('Leia o 1º número: '))
n2 = int(input('Leia o 2º número: '))
n3 = int(input('Leia o 3º número: '))

if (n1 > n2) and (n2 > n3):
    print(f'{n1} é o maior.')
elif (n2 > n3) and (n2 > n1):
    print(f'{n2} é o maior.')
else:
    print(f'{n3} é o maior.')