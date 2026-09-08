numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é \033[36mPAR!!\033[m'.format(numero))
else:
    print('O número {} é \033[31mIMPAR!!\033[m'.format(numero))