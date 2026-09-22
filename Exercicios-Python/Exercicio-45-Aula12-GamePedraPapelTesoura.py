from random import randint # IMPLEMENTAR O COMPUTADOR NO GAME.
from time import sleep # IMPLEMENTAR O TEMPO DE RESPOSTA NA HORA DE IMPRIMIR OS RESULTADOS
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) # FAZ COM QUE O COMPUTADOR ESCOLHA UMA DESSAS ALTERNATIVAS
print('''Suas Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua Jogada? '))
print('JO')
sleep(1) # TEMPO DE RESPOSTA PARA SAIR O RESULTADO DO PRINT.
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 12)
print('Você Jogou {}'.format(itens[jogador])) # FAZ COM QUE MOSTRE O QUE VOCE ESCOLHEU DAS TRES OPÇOES.
print('-=' * 12)
if computador == 0: # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O computador jogou PEDRA! Você GANHOU!')
    elif jogador == 2:
        print('O computador jogou PEDRA! Você PERDEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:  # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('O computador jogou PAPEL! Você PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O computador jogou PAPEL! Você GANHOU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2:  # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('O computador jogou TESOURA! Você GANHOU!')
    elif jogador == 1:
        print('O computador jogou TESURA! Você PERDEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')