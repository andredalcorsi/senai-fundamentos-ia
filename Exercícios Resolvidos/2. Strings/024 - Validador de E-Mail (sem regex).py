'''

024. Leia um e-mail e informe se ele é válido: exatamente um @ , pelo menos um . depois do @ , sem
espaços e sem começar ou terminar com @ ou . .

Dica: .count('@') garante a unicidade; use fatiamento a partir da posição do @ para checar o
domínio.

'''

email = str(input("Digite um endereço de e-mail válido: "))

arroba = "@"

while arroba in email:
    if (arroba > 1):
        email = str(input("Digite um endereço de e-mail válido: "))
    else:

