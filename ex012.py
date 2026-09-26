'''

Leia as coordenadas (x, y) de dois pontos e calcule a distância entre eles. d = √((x2-x1)2 + (y2-
y1)2)

DICA: math.hypot(dx, dy) faz a raiz da soma dos quadrados de uma vez — mas tente antes com
math.sqrt

'''

import math

x1 = float(input('Digite a coordenada X1: '))
x2 = float(input('Digite a coordenada X2: '))
y1 = float(input('Digite a coordenada Y1: '))
y2 = float(input('Digite a coordenada Y2: '))


distancia = (math.sqrt((x2-x1)**2) + (y2-y1)**2)

print(f'A distância entre os pontos é: {distancia:.2f}')