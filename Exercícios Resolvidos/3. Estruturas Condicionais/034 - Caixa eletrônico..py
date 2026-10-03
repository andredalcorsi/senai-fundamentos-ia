'''

034 - Leia um valor de saque entre 10 e 600 e informe quantas notas de 100, 50, 20 e 10 serão
entregues, usando o menor número de cédulas. Recuse valores impossíveis.

Dica: valide primeiro (múltiplo de 10 e dentro da faixa) e só então faça as divisões sucessivas.

'''

saque = float(input('Digite o valor para saque. R$'))

if (10 <= saque <= 600) and (saque >= 10):
    print('Valor dentro da faixa de saque!')
else:
    print('Fora da faixa de saque!')

notasCem = saque // 100
resto = saque % 100

notasCinquenta = resto // 50
resto = resto % 50

notasVinte = resto // 20
resto = resto % 20

notasDez = resto // 10
resto = resto % 10

notasCinco = resto // 5
resto = resto % 5

print(f'Qtde. R$100,00 disponíveis: {notasCem}; \n'
      f'Qtde. R$50,00 disponíveis: {notasCinquenta}; \n'
      f'Qtde. R$20,00 disponíveis: {notasVinte}; \n'
      f'Qtde. R$10,00 disponíveis: {notasDez}.')