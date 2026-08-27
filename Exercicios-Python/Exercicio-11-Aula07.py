larg = float(input('Largura da parede: '))
alt = float(input('Altura da Parede: '))
area = larg * alt
litros = area / 2
print('Sua parede tem a dimensão {} de Largura x {} de Altura 3 e sua área é de {}m²'.format(larg, alt, area))
print('Você precisa de {} litros de tinta para pintar sua parede completa'.format(litros))