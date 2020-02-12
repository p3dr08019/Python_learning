''' 

| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b

'''

lad_A = int(input('Primeiro lado(A): '))
lad_B = int(input('Segundo lado(B): '))
lad_C = int(input('Terceiro lado(C): '))

if abs(lad_B - lad_C) < lad_A < (lad_B + lad_C):

    if abs(lad_A - lad_C) < lad_B < (lad_A + lad_C):

        if abs(lad_A - lad_B) < lad_C < (lad_A + lad_B):
            print('Forma um triangulo')

else:
    print('Nao forma um triangulo')
    pass