class Pessoa:
    
    def __init__(self, nome, idade, cor, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.comendo = comendo
        self.falando = falando
    
    def comer(self, alimento):
        if self.comendo:
            print('{} já está comendo'.format(self.nome))
            return
        print('{} esta comendo {}'.format(self.nome, alimento))
        self.comendo = True
    
    def parar_comer(self, alimento ):
        if self.comendo == True:
            print('{} parou de comer.'.format(self.nome))
        else:
            print('{} nao está comendo.'.format(self.nome))
        self.comendo = False
