'''

Leia três lados; se formarem um triângulo, informe se é equilátero, isósceles ou escaleno.

'''
from traceback import print_exc

primeiroLado = int(input('Digite o primeiro lado do triângulo: '))
segundoLado = int(input('Digite o segundo lado do triângulo: '))
terceiroLado = int(input('Digite o terceiro lado do triângulo: '))

if primeiroLado == segundoLado and segundoLado == terceiroLado and terceiroLado == primeiroLado:
    print('Triângulo Equilátero!')
elif primeiroLado != segundoLado and primeiroLado != terceiroLado and segundoLado != segundoLado:
    print('Triângulo Isósceles!')
else:
    print('Triângulo Escaleno!')