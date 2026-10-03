'''

026 - Leia uma letra e informe se ela é vogal ou consoante.
Dica: converta para minúscula antes de testar, senão A escapa do teste.

'''

letra = str(input('Digite uma letra: '))

if letra in 'aeiou':
    print('Vogal!')
else:
    print('Consoante!')