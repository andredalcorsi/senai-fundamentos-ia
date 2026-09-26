'''
10. Leia peso e altura, calcule o IMC ( peso / altura2 ) e mostre a classificação: abaixo do peso,
normal, sobrepeso ou obesidade.
'''

peso = float(input('Peso em kg: '))
altura = float(input('Algura em cm: '))

imc = peso / ((altura / 100) ** 2)

if (imc < 18.5):
    print('ABAIXO DO PESO!')
elif (imc < 25):
    print('PESO IDEAL')
elif (imc < 30):
    print('SOBREPESO')
elif (imc < 35):
    print('OBESIDADE GRAU I')
elif (imc < 40):
    print('OBESIDADE GRAU II')
else:
    print('OBESIDADE GRAU III (MÓRBIDA)')