# @property, Getters, Setters

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco*(percentual/100))
    
    #Getter
    @property
    def preco(self):
        return self._preco
    
    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))
        self._preco = valor

produto1 = Produto("Camiseta", 99)
produto1.desconto(5)
print(produto1.preco)

produto2 = Produto("Calça", "R$59")
produto2.desconto(15)
print(produto2.preco)
