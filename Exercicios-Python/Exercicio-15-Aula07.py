dias = float(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foi Percorrido durante esses dias? '))
aluguelcarro = 60 * dias
valorkm = 0.15 * km
totalapagar = aluguelcarro + valorkm
print('O Valor do aluguel do carro é: R${:.2f} \nO valor dos Kilometros rodados é: R${:.2f} \nO Total a Pagar: R${:.2f}'.format(aluguelcarro, valorkm, totalapagar))
