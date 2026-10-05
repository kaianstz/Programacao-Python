nome = 'José'  # Cria a variável nome e armazena o texto 'José'.

idade = 33  # Cria a variável idade e armazena o número 33.

print(f'O {nome} tem {idade} anos.')  # Exibe uma mensagem usando uma f-string para inserir os valores das variáveis.

print('O {} tem {} anos.'.format(nome, idade))  # Exibe a mensagem substituindo as chaves pelos valores de nome e idade usando format().

print('O %s tem %d anos.' % (nome, idade))  # Exibe a mensagem usando formatação antiga: %s representa texto e %d representa número inteiro.