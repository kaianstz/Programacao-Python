
resp = 'S'
soma = media = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1 
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numero e a media foi {}'.format(quant, media))
print('O maior numero foi {} e o menor numero foi {}'.format(maior, menor))
