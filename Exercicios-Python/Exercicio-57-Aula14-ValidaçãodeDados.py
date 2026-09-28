sexo = str(input('Informe seu Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Por favor, Informe seu Sexo: ')).strip().upper()[0]
print('Sexo {} Registrado com Sucesso'.format(sexo))
