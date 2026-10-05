n = s = 0  # Cria as variáveis n e s, atribuindo o valor inicial 0 para ambas.

while True:  # Inicia um laço de repetição infinito.
    n = int(input('Digite um Número: '))  # Solicita um número ao usuário e converte o valor para inteiro.

    if n == 999:  # Verifica se o número digitado é igual a 999.
        break  # Interrompe o laço de repetição quando o número 999 é digitado.

    s += n  # Adiciona o valor de n à variável s, acumulando a soma dos números.

print('A soma vale {}'.format(s))  # Exibe na tela o resultado final da soma.
