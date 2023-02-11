# Programação orientada a objetos - POO

# Sintaxe
'''
class Nome:
    objetos de classe
    métodos de classe
    
    
class Nome:
    método construtor
    objetos de classe
    métodos de classe
'''

# Classe Vazia

class Pessoa:
    pass

# Criando objetos fora de uma classe

pessoa1 = Pessoa()

pessoa1.nome = "Fernando"
pessoa1.idade = 32

print(pessoa1.nome)

# Criando funções dentro de uma classe

class Pessoa:
    def acao1(self): # Mesmo uma função sem parametro tem que ter esse self no começo
        print("Ação 1 sendo executada...")
        
pessoa1 = Pessoa()

pessoa1.acao1()

# Criando classe com metodo construtor e objetos internos

class Pessoa:
    def __init__(self, nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura



pessoa2 = Pessoa("Fernando", 32, "M", 1.90)

print(pessoa2.altura)

# Mais de 1 metodo de classe

class Pessoa:
    ano_atual = 2019
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def ano_nascimento(self):
        ano_nasc = self.ano_atual - self.idade
        print(f"Seu ano de nascimento é {ano_nasc}")


pessoa1 = Pessoa("Fernando", 20)

pessoa1.ano_nascimento()


# Metodo de classe fora da classe

class Pessoa:
    ano_atual = 2020
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def ano_nasc(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


pessoa2 = Pessoa.ano_nasc("Fernando", 1999)

print(pessoa2.idade)


# Metodos estaticos
from msilib.schema import Class
from random import randint

class Pessoa:
    @staticmethod
    def gerador_id():
        gerador = randint(100, 999)
        return gerador

print(Pessoa.gerador_id())


# Atributos de classe

class Classe1:
    var1 = 101001


variavel1 = Classe1()

print(Classe1.var1)
print(variavel1.var1)

# Mudando atributo da classe

Classe1.var1 = "Maria"

print(variavel1.var1)


# Encapsulamento

class BaseDeDados:
    def __init__(self):
        self.dados = {}
        #self._dados = {}
        # declaro como protegido (ainda acessivel de fora da classe)
        
        #self.__dados = {}
        # declaro como privado (inacessível e imutável de fora da classe)
        

base = BaseDeDados()

print(base.dados)