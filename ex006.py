'''
6. Leia uma quantidade de segundos e mostre a quantas horas, minutos e segundos ela
corresponde. Ex.: 3760 → 1h 2min 40s
'''

segundos = int(input('Digite a quantidade de segundos que você quer converter: '))

converte_horas = segundos // 3600

resto_horas = segundos % 3600
converte_minutos = resto_horas // 60

resto_minutos = segundos % 60
converte_segundos = resto_minutos

print(f'{round(converte_horas)} hora(s), {round(converte_minutos)} minuto(s) e {round(converte_segundos)} segundos(s).')