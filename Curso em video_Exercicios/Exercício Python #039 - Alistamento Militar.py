from datetime import date
Ano_nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - Ano_nascimento
print(idade)
