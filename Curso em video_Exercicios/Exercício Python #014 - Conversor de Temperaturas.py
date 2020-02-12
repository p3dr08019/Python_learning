# Celsius para Kelvin, Kelvin para Celsius
# K = C + 273
# C = K - 273

# Celsius para Fahrenheit, Fahrenheit para Celsius
# F = 1,8 C + 32
# C = (95 − 32) / 1,8

# Kelvin para Fahrenheit, Fahrenheit para Kelvin
# (K − 273) / 5 = (F − 32) / 9

C = float(input('qual a temperatuta em °C: '))

F = 1.8 * C + 32

print('Temperatura em Fahrenheit: {} °F'.format(round(F, 2)))
