# Importa a função randint, que gera um número inteiro aleatório.
from random import randint

# Cria a variável v com valor inicial 0.
# Ela servirá para contar quantas vezes o jogador venceu.
v = 0

# Inicia um laço infinito.
# O jogo continuará até que o jogador perca.
while True:

    # Pede ao jogador que digite um número.
    # int() transforma o texto digitado em número inteiro.
    jogador = int(input('Digite um Numero: '))

    # O computador escolhe aleatoriamente um número entre 0 e 10.
    computador = randint(0, 10)

    # Soma o número escolhido pelo jogador com o número do computador.
    total = jogador + computador

    # Cria a variável tipo começando com um espaço.
    # Ela armazenará a escolha do jogador:
    # P para Par ou I para Ímpar.
    tipo = ' '

    # Continua pedindo a escolha enquanto ela não for P nem I.
    while tipo not in 'PI':

        # Pede ao jogador que escolha Par ou Ímpar.
        # strip() remove espaços extras no início e no final.
        # upper() transforma a resposta em letra maiúscula.
        # [0] pega somente a primeira letra digitada.
        tipo = str(input('Par ou Impar [P/I] ')).strip().upper()[0]

    # Mostra os números escolhidos pelo jogador e pelo computador,
    # além do resultado da soma.
    # end='' impede que o cursor pule para a próxima linha.
    print(
        f'Voce Jogou {jogador} e o computador jogou {computador}. '
        f'Total deu {total} ',
        end=''
    )

    # Verifica se o total é par ou ímpar.
    # O operador % calcula o resto da divisão.
    # Se o resto da divisão por 2 for 0, o número é par.
    # Caso contrário, o número é ímpar.
    print('DEU PAR !!' if total % 2 == 0 else 'DEU IMPAR !!')

    # Verifica se o jogador escolheu P, ou seja, Par.
    if tipo == 'P':

        # Verifica se o total realmente é par.
        if total % 2 == 0:

            # Informa que o jogador venceu.
            print('Voce Venceu !!')

            # Aumenta a quantidade de vitórias em 1.
            # É equivalente a: v = v + 1
            v += 1

        # Se o total não for par, o jogador perde.
        else:
            print('Voce Perdeu !!')

            # Encerra o laço principal e termina o jogo.
            break

    # Verifica se o jogador escolheu I, ou seja, Ímpar.
    elif tipo == 'I':

        # Verifica se o total é ímpar.
        # Um número ímpar deixa resto 1 quando dividido por 2.
        if total % 2 == 1:

            # Informa que o jogador venceu.
            print('Voce Venceu !!')

            # Aumenta a quantidade de vitórias em 1.
            v += 1

        # Se o total não for ímpar, o jogador perde.
        else:
            print('Voce Perdeu !!')

            # Encerra o jogo.
            break

    # Informa que uma nova rodada começará.
    # Essa linha só é executada se o jogador vencer.
    print('Vamos Jogar Novamente...')

# Mostra a mensagem final do jogo.
# A variável v informa quantas vezes o jogador venceu.
print(f'GAMER OVER! Voce Venceu {v} Vezes.')