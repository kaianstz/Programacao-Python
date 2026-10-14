# Começamos a variável n com o valor 1.
# Esse valor permite que o while seja executado pela primeira vez.
n = 1

# Criamos dois contadores e iniciamos ambos com 0.
# par contará os números pares.
# impar contará os números ímpares.
par = impar = 0

# O laço continuará repetindo enquanto n for diferente de 0.
while n != 0:

    # Pedimos ao usuário que digite um número.
    # A função int() transforma o valor digitado em número inteiro.
    # O número 0 será usado para encerrar o programa.
    n = int(input('Digite um número [0 para parar]: '))

    # Verificamos se o número digitado é diferente de 0.
    # O zero não será contado, pois serve apenas para parar o programa.
    if n != 0:

        # O operador % calcula o resto da divisão.
        # Se o resto da divisão por 2 for 0, o número é par.
        if n % 2 == 0:

            # Aumentamos o contador de números pares em 1.
            # É o mesmo que escrever: par = par + 1
            par += 1

        # Se o número não for par, ele será ímpar.
        else:

            # Aumentamos o contador de números ímpares em 1.
            # É o mesmo que escrever: impar = impar + 1
            impar += 1

# Exibimos a quantidade de números pares e ímpares digitados.
# O método format() coloca os valores de par e impar no texto.
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))