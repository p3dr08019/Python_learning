from random import randint
Preco_Produto = float(input('Qual o preco do produto? '))
valor_desconto = randint(0, 100)
desconto = Preco_Produto * (desc/ 100)
total = Preco_Produto - desconto

print('O produto com um desconto de {}% ' ' e igual a {}' .format(valor_desconto,round(total,2)))