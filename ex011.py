'''
11. Leia capital inicial, taxa mensal e número de meses; mostre o montante final e quanto foi ganho
de juros. M = C·(1 + i)n
'''

capitalInicial = float(input('Informe o capital inicial: R$'))
taxaMensal = float(input('Qual o valor da taxa mensal? '))
qtdeMeses = int(input('Quantidade de parcelas: '))

montanteFinal = capitalInicial * (1 + (taxaMensal / 100) ** qtdeMeses)

print(f'Montante final: {round(montanteFinal,2)} | Quantidade de juros: {round(montanteFinal - capitalInicial,3)}.')