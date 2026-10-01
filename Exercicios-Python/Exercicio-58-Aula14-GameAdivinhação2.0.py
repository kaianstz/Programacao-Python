from random import randint
computador = randint(0, 10)
print('Acerte o numero que o computador está pensando!')
print('Será que voce consegue adivinhar qual o numero?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual o seu Palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente Novamente.')
        elif jogador > computador:
            print('Menos... Tente Novamente.')
print('Após {} Palpites Você Acertou !!!'.format(palpites))
