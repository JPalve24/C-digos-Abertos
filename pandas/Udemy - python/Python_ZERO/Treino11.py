# ESTRUTURA DE REPETIÇÃO 

# While
print("-"*100)
var = 0

while var <= 5:
    print(var)
    var += 1
    
print("-"*100)

# Repetição com condicional

num, total = 1, 10

while num <= 10:
    print(num)
    num += 1
    
    if num == 5:
        print(" 50% Computado")
    if num == total:
        print(" 100%, Processo Encerrado")

print("-"*100)

# Repetição com validação

validador = input("Digite 'Brasil' para Continuar: ")

while validador != "Brasil":
    print("Palavra não confere, digite novamente:")
    validador = input("Digite 'Brasil' para Continuar: ")
    
    if validador == "Brasil":
        print("Agora você digitou corretamente")
        
print("-"*100)

# While True

while True:
    validador = input("Digite 'Brasil' para continuar: ")
    if validador == "Brasil":
        print("Você digitou corretamente!!!")
        break
    else:
        print("Palavra não confere, digite novamente:")
        
# For
print("-"*100)

compras = ["Arroz", "Feijão", "Massa", "Carne", "Pão"]

for i in compras:
    print(i)

print("-"*100)