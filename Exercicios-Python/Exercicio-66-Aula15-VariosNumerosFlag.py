# Cria duas variáveis ao mesmo tempo:
# soma começa com 0 e será usada para armazenar a soma dos números.
# cont começa com 0 e contará quantos números foram digitados.
soma = cont = 0

# Cria um laço infinito.
# Ele continuará repetindo até encontrar um comando break.
while True:

    # Exibe uma mensagem para o usuário digitar um número.
    # A função input() sempre retorna texto.
    # A função int() converte esse texto para um número inteiro.
    num = int(input('Digite um Numero (999 para parar): '))

    # Verifica se o número digitado é igual a 999.
    # O número 999 é o valor utilizado como sinalizador de parada.
    if num == 999:

        # Interrompe imediatamente o laço while.
        # O número 999 não será contado nem somado.
        break

    # Aumenta o valor de cont em 1.
    # É o mesmo que escrever: cont = cont + 1
    cont += 1

    # Adiciona o número digitado ao valor de soma.
    # É o mesmo que escrever: soma = soma + num
    soma += num

# Exibe o resultado final na tela.
# O f antes das aspas permite colocar variáveis dentro do texto.
# {cont} será substituído pela quantidade de números digitados.
# {soma} será substituído pelo resultado da soma.
print(f'A soma dos {cont} Numeros Digitados foi {soma}!')