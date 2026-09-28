n = 1 # Sempre que for usar o WHILE  tem que colocar o N = 1 ou 0
par = impar = 0 # AS VARIAVEIS TAMBEM TEM QUE COLOCAR UM VALOR
while n != : # WHILE ->(enquanto) = n != ->(for diferente de) 0. OU SEJA QUANDO O NUMERO DIGITADO É DIFERENTE DE 0 A REPETIÇAO CONTINUA, QUANDO FOR 0 ELA PARA.
    if n != 0: # FAZ COM QUE O ALGORITIMO NÃO COLOQUE O 0 COMO UM NUMERO PAR.
        if n % 2 == 0: # se o resto da divisão de 2 for igual a 0. ou seja todo numero que for divido por 2 der resultado 0 ele é par.
            par += 1 # aqui ele vai contar quantos numeros par tiverem quando for digitados todos os numeros.
        else:
            impar += 1 # senão aqui ele vai contar quantos numeros impares tiverem quando for digitados todos os numeros.
print('Voce Digitou {} Numeros Pares e {} Numeros Impares!'.format(par, impar))