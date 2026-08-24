real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.14
iene = real / 0.032
euro = real / 5.99
yuan = real / 0.76
print('Com R${} você pode comprar US$ {:.2f}\nVocê poder comprar EUR {:.2f}\nVocê pode comprar JPY {:.2f}\nVoce pode comprar CNY {:.2f}'.format(real, dolar, euro, iene, yuan))