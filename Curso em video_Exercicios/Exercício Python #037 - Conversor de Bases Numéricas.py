Numero = int(input('Digite um numero:'))
print('Para qual base voce deseja converter?: \n 1 para binario \n 2 para octal \n 3 para hexadecimal')
escolha = int(input())


def Binario(Numero):

    binario = ''
    while (Numero > 1):
        Numero/2
    # print(str('O resto da divisao de {} por 2 é: {}'.format(Numero, Numero % 2)))
        binario += str(Numero % 2)
        Numero = Numero//2
        # print(int(Numero % 2))
    binario += str(Numero)
    # print(str('O resultado da ultima divisao e {}'.format(Numero)))

    novo_binario = ''
    for n in range(len(binario)-1, -1, -1):
        novo_binario += binario[n]
    print('{} em binario e igual a: {}'.format(Numero, novo_binario))
    pass


def Octal(Numero):
    octal = ''
    while (Numero > 1):
        Numero/8
    # print(str('O resto da divisao de {} por 2 é: {}'.format(Numero, Numero % 2)))
        octal += str(Numero % 8)
        Numero = Numero//8
        # print(int(Numero % 2))
    octal += str(Numero)
    # print(str('O resultado da ultima divisao e {}'.format(Numero)))

    novo_octal = ''

    for n in range(len(octal)-1, -1, -1):
        novo_octal += octal[n]
    print('{} em octal e igual a: {}'.format(Numero, novo_octal))

    pass


def Hexadecimal(Numero):
    hexadecimal = ''
    while (Numero > 1):
        Numero/16
    # print(str('O resto da divisao de {} por 2 é: {}'.format(Numero, Numero % 2)))
        hexadecimal += str(Numero % 16)
        Numero = Numero//16
        # print(int(Numero % 2))
    hexadecimal += str(Numero)
    # print(str('O resultado da ultima divisao e {}'.format(Numero)))

    novo_hexadecimal = ''
    for n in range(len(hexadecimal)-1, -1, -1):
        novo_hexadecimal += hexadecimal[n]
    print('{} em hexadecimal e igual a: {}'.format(Numero, novo_hexadecimal))
    pass


if (escolha == 1):
    print('voce escolheu a conversao para binario')
    Binario(Numero)
elif (escolha == 2):
    print('voce escolheu a conversao para octal')
    Octal(Numero)
elif (escolha == 3):
    print('voce escolheu a conversao para hexadecimal')
    Hexadecimal(Numero)
else:
    print('Voce nao escolheu um numero correspondente!')
