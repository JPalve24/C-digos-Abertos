# Parametros padrão como False

class Pessoa:
    def __init__(self, nome, idade, sexo=False, altura=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        
pessoa1 = Pessoa("Fernando", 33)

print(pessoa1.nome)

# Classe como molde para criar objetos

class Pessoa:
    def __init__(self, nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

pessoa1 = Pessoa("Mariana", 32, "F", 1.76)
print(pessoa1.nome)
print(pessoa1.altura)

pessoa2 = Pessoa("Gilberto", 33, "M", 1.90)
print(pessoa2.nome)
print(pessoa2.idade)

# Aplicação de Orientação a Objetos

class BaseDeDados:
    def __init__(self):
        self.base = {}
        
    def inserir(self, nome, fone):
        if "clientes" not in self.base:
            self.base["clientes"] = {nome:fone}
        else:
            self.base["clientes"].update({nome:fone})
    
    def listar(self):
        for nome, fone in self.base["clientes"].items():
            print(nome, fone)
    
    def apagar(self, nome):
        del self.base["clientes"][nome]



