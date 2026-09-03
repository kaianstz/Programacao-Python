tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('--Fim--')
#tambem pode fazer dessa forma: print('Carro Novo'if tempo<=3 else'Carro Velho') 
nome = str(input('Qual é seu nome? '))
if nome == 'Kaian':
    print('Que Bonito nome voce tem!')
else:
    print('Seu nome é tão normal!')
print('Bom Dia, {}!'.format(nome))

n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))
media = (n1 + n2)/2
print('Sua Media é: {:.1f}'.format(media))
if media >= 6.0:
    print('Você Teve uma média suficiente então está APROVADO!')
else:
    print('Você teve uma média Insuficiente então está REPROVADO!')