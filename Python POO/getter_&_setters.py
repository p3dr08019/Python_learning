class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))


p1 = Produto('Camisa', 50)
p1.desconto(10)
print(p1.preco)