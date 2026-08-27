preco = float(input('Qual é o Valor do Produto? R$'))
novopreco = preco * 0.95 # ou novopreco = preco - (preco * 5 / 100)
print('O novo valor com 5% de desconto é: R$ {:.2f}'.format(novopreco))
