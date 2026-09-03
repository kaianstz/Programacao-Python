from random import randint
from time import sleep #FAZ O COMPUTADOR ESPERAR ALGUNS SEGUNDOS ATÉ DAR A RESPOSTA.
pc = randint(0, 5) # FAZ O COMPUTADOR ESCOLHER UM NUMERO ALEATORIO.
eu = int(input('Qual numero de 0 a 5 O computador está pensando? '))
print('PROCESSANDO...')
sleep(3) #FAZ O COMPUTADOR ESPERAR 3 SEGUNDOS ATÉ DAR A RESPOSTA.
if eu == pc:
    print('Você Acertou Parabens!!!!')
else:
    print('Você Errou !!!')
    print('O Computador pensou no número: {} Tente novamente.'.format(pc))
