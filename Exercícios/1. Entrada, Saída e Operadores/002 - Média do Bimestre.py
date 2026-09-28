'''
2. Leia 6 notas diferentes e mostre a média final do aluno.
'''

contador = 0
soma = 0
media = 0

while (contador < 6):
    notas = float(input('Digite sua nota: '))
    soma += notas
    contador+=1

media = float(soma / 6)

print(f'Media: {round(media, 2)}')

