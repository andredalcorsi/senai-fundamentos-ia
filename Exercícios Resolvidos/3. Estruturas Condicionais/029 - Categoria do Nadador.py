'''

029 - Leia a idade de um atleta e classifique-o: até 9 mirim, até 14 infantil, até 19 júnior, até 25 sênior,
acima disso master.

Dica: ordem crescente com elif evita que uma faixa "engula" a outra.

'''
while True:
    try:
        idade = int(input('Digite a idade de um atleta: '))
        break
    except ValueError:
        print('Só aceitamos números!')

if (idade <= 9):
    print('Mirim!')
elif (idade <= 14):
    print('Infantil!')
elif (idade <= 19):
    print('Junior!')
else:
    print('Senior!')