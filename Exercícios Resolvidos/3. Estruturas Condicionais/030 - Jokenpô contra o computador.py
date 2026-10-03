'''

030 - Crie um jogo de pedra, papel e tesoura contra o computador usando random.randint, exibindo a
jogada de cada um e o resultado.

Dica: trate primeiro o caso de empate; sobram só três combinações de vitória para o jogador.

'''

import random

print('========================== JOKENPO =====================================')

itens = ['', 'Pedra', 'Papel', 'Tesoura']

jogador = int(input('[1] PEDRA\n'
                    '[2] PAPEL\n'
                    '[3] TESOURA\n'
                    'Faça sua escolha: '))

while (jogador > 3) or (jogador < 1):
    jogador = int(input('[1] PEDRA\n'
                        '[2] PAPEL\n'
                        '[3] TESOURA\n'
                        'Faça sua escolha: '))

pc = random.randint(1, 3)

print(f'Jogador: {itens[jogador]} x PC: {itens[pc]}')

if jogador == pc:
    print('EMPATE!')
elif (jogador == 1 and pc == 2) or (jogador == 2 and pc == 3) or (jogador == 3 and pc == 1):
    print('PC GANHOU!')
else:
    print("JOGADOR GANHOU!")