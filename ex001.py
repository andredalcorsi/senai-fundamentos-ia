'''
1. Leia o nome, a idade e a cidade de nascimento de uma pessoa e exiba tudo em uma única frase.
- Saída esperada: Meu nome é Luis Tatin, tenho 22 anos e nasci em São Bernardo do Campo
'''


nome = input('Digite seu nome: ')
idade = int(input('Diga sua idade: '))
cidade = input('Você mora em qual cidade? ')

print(f'Olá, {nome}! Você tem {idade} anos e mora em {cidade}.')