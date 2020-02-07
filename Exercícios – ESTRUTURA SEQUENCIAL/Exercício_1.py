# Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)

speed_ms = int(input('leitor de velocidade: '))
conversor = 3.6
speed_kmh = speed_ms/conversor
print('Voce atingiu uma velocidade em Km/h de: {}'.format(round(speed_kmh,1)))