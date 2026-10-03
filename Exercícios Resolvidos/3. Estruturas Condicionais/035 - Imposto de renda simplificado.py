'''

035 - Leia o salário mensal e calcule o imposto por faixas progressivas: até 2.000 isento, até 3.000
paga 7,5% sobre o excedente, até 4.500 paga 15% sobre o excedente, acima disso 22,5%.

Dica: o imposto incide apenas sobre a parte do salário dentro de cada faixa — não sobre o total.

'''

salarioMensal = float(input('Informe seu salário. R$'))

while (salarioMensal <= 0):
    salarioMensal = float(input('Informe o seu salário. R$'))

if (salarioMensal <= 2000):
    print(f'ISENTO')
elif (salarioMensal <= 3000):
    taxa = (salarioMensal * (7.5/100))
    print(f'Valor do imposto: {taxa}')
elif (salarioMensal <= 4500):
    taxa = (salarioMensal * (15/100))
    print(f'Valor do imposto: {taxa}')
else:
    taxa = (salarioMensal * (22.5/100))
    print(f'Valor do imposto: {taxa}')