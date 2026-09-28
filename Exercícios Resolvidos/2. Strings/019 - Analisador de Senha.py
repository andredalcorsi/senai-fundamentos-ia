'''
19. Leia uma senha e informe se ela é forte: mínimo 8 caracteres, ao menos uma letra maiúscula,
uma minúscula e um dígito.
'''
maiuscula = False
minuscula = False
numero = False 

senha = str(input('Digite sua senha: '))

for caractere in senha: 
    if caractere.isupper():
        maiuscula = True
    if caractere.islower():
        minuscula = True
    if caractere.isdigit():
        numero = True

if (len(senha) >= 8) and (maiuscula) and (minuscula) and (numero):
    print('Senha Forte!')
else: 
    print('Senha Fraca. Tente novamente.')