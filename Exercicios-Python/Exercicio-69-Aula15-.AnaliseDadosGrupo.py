# Cria três contadores e inicia todos com o valor 0.
#
# tot18: contará quantas pessoas têm 18 anos ou mais.
# totH: contará quantos homens foram cadastrados.
# totM20: contará quantas mulheres têm menos de 20 anos.
tot18 = totH = totM20 = 0


# Inicia um laço infinito para cadastrar várias pessoas.
# O laço só será encerrado quando o usuário escolher "N".
while True:

    # Mostra uma linha formada por 20 caracteres "-".
    # O operador * repete o texto 20 vezes.
    print('-' * 20)

    # Exibe o título da área de cadastro.
    print('CADASTRE UMA PESSOA')

    # Mostra uma linha formada por 20 caracteres "~".
    print('~' * 20)

    # Pede a idade da pessoa.
    # input() recebe um texto.
    # int() converte o texto para um número inteiro.
    idade = int(input('Digite a Idade: '))

    # Cria a variável sexo começando com um espaço.
    # Ela será usada para armazenar "M" ou "F".
    sexo = ' '

    # Continua perguntando o sexo enquanto a resposta
    # não for "M" nem "F".
    while sexo not in 'MF':

        # Pede o sexo da pessoa.
        #
        # str() garante que o valor seja tratado como texto.
        # strip() remove espaços extras.
        # upper() transforma a resposta em letra maiúscula.
        # [0] pega apenas o primeiro caractere digitado.
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    # Verifica se a idade é maior ou igual a 18.
    if idade >= 18:

        # Adiciona 1 ao contador de pessoas com 18 anos ou mais.
        # É equivalente a: tot18 = tot18 + 1
        tot18 += 1

    # Verifica se o sexo informado foi "M".
    if sexo == 'M':

        # Adiciona 1 ao contador de homens.
        # É equivalente a: totH = totH + 1
        totH += 1

    # Verifica duas condições ao mesmo tempo:
    #
    # 1. A pessoa precisa ser mulher: sexo == 'F'
    # 2. A mulher precisa ter menos de 20 anos: idade < 20
    if sexo == 'F' and idade < 20:

        # Adiciona 1 ao contador de mulheres com menos de 20 anos.
        totM20 += 1

        # Mostra uma linha separadora.
        print('-' * 20)

    # Cria a variável resp começando com um espaço.
    # Ela armazenará a resposta sobre continuar ou não o cadastro.
    resp = ' '

    # Continua perguntando enquanto a resposta não for "S" nem "N".
    while resp not in 'SN':

        # Pergunta se o usuário deseja continuar.
        #
        # strip() remove espaços extras.
        # upper() transforma a resposta em maiúscula.
        # [0] pega apenas o primeiro caractere.
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]

    # Verifica se o usuário respondeu "N".
    if resp == "N":

        # Encerra o laço principal.
        # Com isso, o programa para de cadastrar pessoas.
        break


# Exibe a quantidade de pessoas com 18 anos ou mais.
print(f'Total de pessoas com mais de 18 anos: {tot18}')

# Exibe a quantidade total de homens cadastrados.
print(f'Ao todo temos {totH} Homens cadastrados')

# Exibe a quantidade de mulheres com menos de 20 anos.
print(f'E temos {totM20} Mulheres com menos de 20 anos')