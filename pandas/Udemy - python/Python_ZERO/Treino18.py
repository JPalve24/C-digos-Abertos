# FUNÇÕES

# Sintaxe

def nome(parametro):
    "Corpo da Função"
    
def minha_funcao():
    print("Minha Primeira Função!!!")
    

minha_funcao()

# Função que inicialmente não faz nada

def funcao(): # para deixar a funcao para ser feita depois
    pass 

var1 = funcao()

print(type(var1))

# Função interagindo com o usuario

usuario3 = input("Digite seu Nome: ")

def mensagem(nome):
    print(f"Bem-vindo {nome}!!!")
    

mensagem(usuario3)

# Parametrizando função via variavel

def funcao(msg):
    print(msg)


funcao("Olá Rapaz")

# Funcao com mais de um parametro

def mensagem(nome, idade):
    print(f"{nome} tem {idade} anos...")


mensagem("João Paulo", 22)

# Definindo parametros "Padrão"

def funcao(msg = "???", nome = "usuário"):
    print(f"{msg} para {nome}")

funcao("Email", "Jpasn")

# Descrevendo "Padrão"

def funcao(msg = "Olá", nome = "usuário", msg2 = "Seja bem-vindo"):
    print(msg, nome, msg2)

funcao(nome = "Fernando")

# Passando parâmetro e interagindo com o usuário

def funcao(mensagem = "Oi", nome = "Desconhecido"):
    print(mensagem, nome)


funcao("Olá", input("Digite seu nome: "))

# Variavel dentro de funções

def funcao(msg = "Olá", nome = "usuário", msg2 = "Seja bem-vindo"):
    nome = input("Digite seu nome: ")

var = funcao()

# return

def funcao(msg = "Olá", nome = "usuário", msg2 = "Seja bem-vindo"):
    return f"{msg} {nome}, {msg2}"

var = funcao()

print(var)


# Operações em funções

def soma(n1 = 0, n2 = 0):
    return f"A soma de {n1} com {n2} é {n1 + n2}"

print(soma(5, 3))

# Equações em funções

def aumento_percentual(valor = 0, percentual = 0):
    return (valor + (valor * percentual / 100))

num1, num2 = float(input("Digite o valor: ")), float(input("Digite o % a ser somado: "))

calculo = aumento_percentual(num1, num2)

print(f"O valor final é de {calculo}")
print(f"O valor final será: {round(calculo, 2)} reais")
print(f"O valor final será: R$ {calculo:,.2f}")


# Repetição em funções

def repetidor(msg):
    contador = 0
    while contador < 5:
        print(msg)
        contador += 1

repetidor("OLÁ")

# Condicionais em funções

def divisao(n1 = 0, n2 = 0):
    if n1 == 0 or n2 == 0:
        return "Operação Inválida"
    return n1 / n2

print(f"O resultado da divisão é {divisao(5)}")


# Funções com argumentos externos

def funcao(*args):
    for parametro in args:
        print(parametro)


argumentos = ("Nome", "Idade")

funcao(argumentos)

# Desempacotando uma lista para elementos de uma função

lista1 = ["nome", "idade", "sexo", "nacionalidade"]

def  funcao(*args):
    print("Informações Necessárias")
    print(args)
    
    
funcao(*lista1)    

# Função com parametros baseados em *args e **kwargs

# Supondo que esta cadastrando senha e usuario

def funcao(*args, **kwargs):
    print(args)
    print(kwargs)
    
senhas_padrao = [12345, 11111, 54321]

resultado = funcao(*senhas_padrao, usuario = "user", administrador = "admin")

print(resultado)

# Buscando dados do modelo anterior

def funcao(*args, **kwargs):
    nome = kwargs["usuario"]
    nome2 = kwargs["administrador"]
    senha1 = args[0]
    senha2 = args[1]
    
    print(f"O usuário padrão é: {nome}")
    print(f"O administrador é: {nome2}")
    print(f"A senha padrão é: {senha1}")
    print(f"A senha alternativa é: {senha2}")
    

senhas_padrao = [12345, 11111]

funcao(*senhas_padrao, usuario = "user", administrador = "admin")

# Função que recebe outra função

def mestre(funcao):
    return funcao()

def msg_boas_vindas():
    return "Seja Bem-Vindo!!!"

executa = mestre(msg_boas_vindas)

print(executa)

# Funções Lambda

numero1 = int(input("Digite um Número: "))
numero2 = int(input("Digite outro Número: "))

var = lambda num1, num2: num1 * num2

print(var(numero1, numero2))

# Escopo global e Escopo local

variavel1 = "Paulo"

def funcao1():
    print(f"variavel do escopo global: {variavel1}")

funcao1()

def funcao2():
    variavel2 = "Maria"
    print(f"variavel do escopo local: {variavel2}")

funcao2()

# Modificando uma variavel global por meio de uma função

num1 = 100

print(f"variavel com valor inicial: {num1}")

def modificador():
    global num1
    num1 = 200
    print(f"variavel dentro da função: {num1}")

modificador()

print(f"variavel com valor final: {num1}")