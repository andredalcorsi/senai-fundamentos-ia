'''

Leia um CPF no formato 12345678900 e exiba-o como 123.456.789-00 .


'''

cpf = str(input('Digite seu cpf (somente números): '))

print(f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}')
