# Calcule a area da parede a partir de 2 entradas, altura e largura. Mostre a quantidade de tinta usada obs. 2m^2 = 1L tinta

H = float(input('Qual a altura da parede? '))
B = float(input('Qual a largura da parede? '))

Area = H * B
L = Area / 2
print('A area da parede e de {} m²' .format(Area))
print('Voce usará {} litros de tinta para pintar a parede' .format(L))