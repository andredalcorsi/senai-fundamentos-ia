'''
8. Leia o salário de um funcionário e o percentual de aumento; mostre o valor do aumento e o novo
salário formatado com duas casas decimais.
'''

salario = float(input('Digite seu salário: '))
percentual = float(input('Qual a porcentagem de aumento: '))

novo_salario = salario * (percentual/100) + salario

print(f'Salário Antigo: R${round(salario,2)} | Novo Salário: R${round(novo_salario,2)}')