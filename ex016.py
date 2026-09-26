'''

16. Leia uma palavra e mostre-a escrita de trás para frente.

DICA: o fatiamento aceita passo negativo: palavra[::-1] .

'''


palavra = str(input('Digite uma palavra: '))

contrario = palavra[::-1]

print(f'Palavra escrita: {palavra} | Ao Contrário: {contrario}')
