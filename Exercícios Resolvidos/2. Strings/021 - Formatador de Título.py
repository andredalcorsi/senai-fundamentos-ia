'''
021. Leia uma frase bagunçada (com espaços sobrando nas pontas e capitalização aleatória) e
devolva-a limpa, com cada palavra iniciando em maiúscula.

Dica: .strip()  limpa as bordas e  .title()  ajusta as iniciais
'''

frase = str(input('Digite uma frase: ')).strip().title()

print(frase)