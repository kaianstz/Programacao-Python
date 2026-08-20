nota1 = float(input('Digite a Primeira Nota: '))
nota2 = float(input('Digite a Segunda Nota: '))
soma = nota1 + nota2
media = soma / 2
# ou media = (n1 + n2) / 2  - mesmo resultado sem colocar a variavel soma
print('A Média é: {:.1f}'.format(media))
