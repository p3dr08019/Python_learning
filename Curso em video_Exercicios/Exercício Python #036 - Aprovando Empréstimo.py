import autopep8


def Aprovacao_Emprestimo():
    if (mensalidade <= salario * 0.3):
        print('Emprestimo aprovado')
    else:
        print('Emprestimo negado')


valor_casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salario?'))
tempo_pagamento = int(input('Em quantos anos voce deseja paga a casa?'))

anos_para_meses = tempo_pagamento * 12
mensalidade = round(valor_casa / (tempo_pagamento * 12), 2)

Aprovacao_Emprestimo()
