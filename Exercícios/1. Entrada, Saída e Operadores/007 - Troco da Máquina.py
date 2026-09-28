'''

7. Leia um valor inteiro em centavos e mostre quantas moedas de 50, 25, 10, 5 e 1 centavo são
necessárias usando o menor número de moedas.

'''

centavos = float(input('Quantos centavos você tem aí? '))

cinquenta = centavos // 50
resto_cinquenta = centavos % 50

vinte_cinco = resto_cinquenta // 25
resto_vinteecinco = resto_cinquenta % 25

dez = resto_vinteecinco // 10
resto_dez = resto_vinteecinco % 10

cinco = resto_dez // 5
resto_cinco = resto_dez % 5

um = resto_cinco

print(f'CINQUENTA CENTAVOS: {cinquenta}\n'
      f'VINTE E CINCO CENTAVOS: {vinte_cinco}\n'
      f'DEZ CENTAVOS: {dez}\n'
      f'CINCO CENTAVOS: {cinco}\n'
      f'UM CENTAVO: {um}')