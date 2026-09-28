'''

17. Leia o nome completo e mostre apenas as iniciais em maiúsculo. Ex.: Luis Eulalio Tatin →
L.E.T.

'''

nome = str(input('Diga seu nome: '))

nome_fatiado = nome.split()

firstIni = nome_fatiado[0]
secondIni = nome_fatiado[1]
thirdIni = nome_fatiado[2]

print(f'Nome digitado: {nome} | Iniciais: {firstIni[0]}.{secondIni[0]}.{thirdIni[0]}.')