'''

032 - Leia o peso de uma encomenda e o estado de destino; calcule o frete conforme a faixa de peso,
com 20% de acréscimo se o destino não for do Sudeste.

Dica: defina o valor base no if das faixas e aplique o acréscimo depois, em um teste separado.

'''



peso = float(input('Digite o peso da encomenda: '))
estadoDestino = str(input('Informe o estado destino: '))

if peso <= 5:
    frete = 50.0
elif peso <= 10:
    frete = 100.00
elif peso <= 25:
    frete = 150.00
else:
    frete = 200.00
    
if (peso <= 10 and estadoDestino == "sudeste"):
    print(f'O valor do frete é R${frete}.')
elif (estadoDestino != "sudeste"):
    frete_convertido = (frete * (20/100)) + frete
    print(f'O valor do frete é R${frete_convertido}')

