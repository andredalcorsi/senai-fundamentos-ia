'''
20. Leia uma frase e mostre quantas vogais, quantas consoantes e quantos espaços ela tem.
'''

qtde_vogais = 0
qtde_consoantes = 0 
qtde_espacos = 0 

frase = str(input('Digite uma frase: '))

for caracteres in frase: 
    c = caracteres.lower()

    if c in 'aeiouáéíóúâêîôûãõà':
        qtde_vogais+=1
    if c.isalpha():
        qtde_consoantes+=1
    if c.isspace():
        qtde_espacos+=1

print(f'Vogais: {qtde_vogais}\n'
      f'Consoantes: {qtde_consoantes}\n'
      f'Espaços: {qtde_espacos}')

        



