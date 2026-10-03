'''

027 - Leia duas notas, calcule a média e informe: aprovado (≥ 7), recuperação (≥ 5) ou reprovado.

Dica: teste do maior para o menor com elif ; assim você não precisa repetir os limites inferiores.

'''

contador = 0
acumula_nota = 0

while contador < 2:
    nota = float(input('Digite uma nota: '))
    contador+=1
    acumula_nota = acumula_nota + nota

media = (acumula_nota / 2)

if media >= 7:
    print(f'Aprovado!')
elif media >= 5:
    print('Recuperação1')
else:
    print('Reprovado!')


