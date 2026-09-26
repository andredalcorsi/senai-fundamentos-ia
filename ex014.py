'''

14. Leia uma frase e mostre quantas vezes a letra "a" aparece, em que posição aparece pela
primeira vez e em que posição aparece pela última.

'''

frase = str(input('Digite uma frase: ')).upper()

print(f'Quantas vezes a letra "A" aparece: {frase.count('a')}\n')
print(f'Primeira vez que a letra "A" aparece: {frase.find('a')}\n')
print(f'Posição em que "A" aparece pela última vez: {frase.rfind('a')}\n')