valorcasa = float(input('Qual o valor da casa que deseja comprar: R$ '))
salario = float(input('Digite o seu salario: R$ '))
anos = int(input('Em quantos anos deseja financiar? '))
prestaçao = valorcasa / (anos * 12) # valor da casa dividido pela quantidade de anos desejado.
minimo = salario * 0.30 # minimu de 30 % do salario para o financiamento ser aprovado.
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação é de R$ {:.2f}'.format(valorcasa, anos, prestaçao))
if prestaçao <= minimo: # se o valor da prestaçao for menor ou igual que o minimo de 30%  o emprestimo é aprovado, se nao reprovado.
    print('O empréstimo pode ser APROVADO!')
else:
    print('O empréstimo está NEGADO o valor da prestação é maior que o minimo permitido.')