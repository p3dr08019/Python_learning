# Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

Total_Minutos = int(input('Quantos minutos? '))

hora = int(Total_Minutos / 60)
minutos = Total_Minutos%60

print('Agora sao exatamente: {} horas e {} minutos' .format(hora, minutos))

