velocidade = float(input('qual é a velocidade do atual do carro? '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('\033[1;31mVoce foi MULTADO!!!\033[m Por está acima da velocidade permitida e receberá a multa no valor de \033[31mR$ {}\033[m159 \n\033[33mTome cuidado e Tenha uma Boa Viagem!!!\033[m'.format(multa))
else:
    print('\033[32mVocê está na velocidade permitida!! Tenha uma Boa Viagem!!!\033[m')