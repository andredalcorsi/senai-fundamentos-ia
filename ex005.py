'''
5. Leia o raio de uma esfera e calcule volume e área. V = (4/3)·π·r3 e A = 4·π·r2
'''

raio = float(input('Digite o raio da esfera: '))

V = ((4/3) * 3.14) * (raio ** 3)
A = (4 * 3.14) * (raio ** 2)

print(f'Volume: {round(V,2)} | Área: {round(A,2)}')