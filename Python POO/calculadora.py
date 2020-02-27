class calculator:
    def __init__(self, a, b, result = str()):
        self.a = a
        self.b = b
        self.result = result

    def som(self):
        return print(self.a + self.b)

    def sub(self):
        return print(self.a - self.b)

    def mult(self):
        return print(self.a * self.b)

    def div(self):
        if self.b == 0:
            print('nao pode ser dividido por zero')
            return
        else:
            print(round((self.a / self.b), 2))

c = calculator(int(input('primeiro valor: ')), int(input('segundo valor: ')), str(input('o  que voce deseja fazer? ')))

if c.result in 'soma +':
    c.som()
    pass
elif c.result in 'subtrair -':
    c.sub()
    pass
elif c.result == 'multiplicar *':
    c.mult()
    pass
elif c.result == 'dividir /':
    c.div()
    pass


