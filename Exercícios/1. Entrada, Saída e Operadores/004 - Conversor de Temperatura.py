'''
4. Leia uma temperatura em graus Celsius e converta para Fahrenheit. F = C × 9/5 + 32
'''

temperatura = float(input('Digite a temperatura: '))

F = ((temperatura *9)/5) + 32

print(f'Temperatura em Celsius: {round(temperatura, 2)}ºC | Temperatura convertida em Fahrenheit: {round(F, 2)}ºF.')

