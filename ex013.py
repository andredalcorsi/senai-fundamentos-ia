'''

13. Leia o nome completo de uma pessoa e mostre: (1) tudo em maiúsculas, (2) tudo em minúsculas,
(3) quantas letras ao todo sem contar os espaços, (4) quantas letras tem o primeiro nome.

'''

nome = str(input('Digite seu nome completo: ')).strip()

print(f'1. Tudo em maiúsculas: {nome.upper()}')
print(f'2. Tudo em minúsculas: {nome.lower()}')

noSpace = nome.replace(' ', '')

print(f'3. Quantidade de letras sem contar espaço: {len(noSpace)}')

palavras = nome.split()
primeiroNome = palavras[0]

print(f'4. Quantas letras tem o primeiro nome: {len(primeiroNome)}')