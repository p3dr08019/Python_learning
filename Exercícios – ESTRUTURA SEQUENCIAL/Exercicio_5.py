# Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).

numero = int(input('digite um numero de 3 digitos: '))
soma = 0
while(numero != 0):
    soma += numero%10
    numero = int(numero/ 10)
    
print('A soma dos algarismos e igual a: {}'.format(soma))

