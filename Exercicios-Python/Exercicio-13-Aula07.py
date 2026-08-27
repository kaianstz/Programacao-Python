salario = float(input('Digite o salário do funcionario R$'))
novosalario = salario * 1.15 # ou novosalario = salario + (salario * 15 / 100)
print('O funcinario tinha o salario de R$ {:.2f} e com 15% de aumento, passa a receber R$ {:.2f}'.format(salario, novosalario))