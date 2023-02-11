# ESTRUTURA CONDICIONAL SIMPLES

# If
print("-"*100)

nome = input("Digite seu nome: ")

if nome == "Fernando":
    print("Bem-Vindo de volta, Fernando!")
    
print(f"Você é novo aqui, olá {nome}")

print("-"*100)

# Else

numero = int(input("Digite seu numero: "))

if numero < 50:
    print("Menor que 50")
else:
    print("Maior que 50")
    
print("-"*100)

# Elif

num1 = float(input("Digite seu numero: "))

if num1 < 50:
    print("Menor que 50")
elif num1 == 50:
    print("Igual a 50")
elif num1 > 50 and num1 < 100:
    print("Maior que 50")
else:
    print("Número inválido")
 
print("-"*100)

# Condicional com 1 desfecho

nome1, nome2 = "Fernando", "Maria"

if nome1 == "Fernando":
    print("Bem-Vindo, Fernando!!!")
elif nome2 == "Maria":
    print("Bem-Vinda, Maria!!!")
else:
    print("ERRO, Nome Inválido")  
    
print("-"*100)

# Condicional com mais de 1 desfecho

nome1, nome2 = "Fernando", "Maria"

if nome1 == "Fernando":
    print("Bem-Vindo, Fernando!!!")
if nome2 == "Maria":
    print("Bem-Vinda, Maria!!!")
else:
    print("ERRO, Nome Inválido")  

print("-"*100)

# Condicional de interpolação

nomes, usuario = ["Fernando", "Maria", "Carlos"], input("Digite seu nome: ")

if usuario in nomes:
    print(f"Bem-Vindo(a), {usuario}.")
else:
    print("Usuário não cadastrado.")
    
print("-"*100)

# Condicionais com validação simples

nome = input("Digite seu nome: ")

if nome == "Fernando":
    print("Olá Fernando, Você é o Administrador do Sistema!")
elif nome in "Ana Barbara Carlos José Maria Paulo Tatiana":
    print(f"Bem-vindo(a) {nome}, você já está cadastrado(a)!")
else:
    print("Olá, você não está logado!")
    
print("-"*100)

# Multiplos Elifs

nome = input("Digite seu nome: ")

if nome == "Fernando":
    print("Olá Fernando, Você é o Administrador do Sistema!")
elif nome in "Ana Barbara Maria Tatiana":
    print(f"Bem-vinda {nome}, você já está cadastrada!")
elif nome in "Carlos José Paulo":
    print(f"Bem-vindo {nome}, você já está cadastrado!")   
else:
    print("Olá, você não está logado!")
    
print("-"*100)

# Multiplos Elifs atribuidos a variaveis

nome = input("Digite seu nome: ")

funcionarios = ["Carlos", "José", "Paulo"]
funcionarias = ["Ana", "Barbara", "Maria", "Tatiana"]

if nome == "Fernando":
    print("Olá Fernando, Você é o Administrador do Sistema!")
elif nome in funcionarias:
    print(f"Bem-vinda {nome}, você já está cadastrada!")
elif nome in funcionarios:
    print(f"Bem-vindo {nome}, você já está cadastrado!")   
else:
    print("Olá, você não está logado!")
    
print("-"*100)