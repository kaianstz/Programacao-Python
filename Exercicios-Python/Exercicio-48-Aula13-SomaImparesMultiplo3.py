soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # TAMBEM PODE SER: cont += 1
        soma = soma + c # TAMBEM PODE SER: soma += c
print ('A soma de todos os {} Valores solicitados é: {}'.format(cont, soma))