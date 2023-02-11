# Função de Saída que Exibe em Tela ou em Terminal

print("Seja Bem-Vindo!!!")

nome = "Fernando"
print(nome)

# Realizando operações dentro da função print()

print(15+2)
print(15-4)
print(15*2)
print(15/4)

# Realizando Operações Entre Dados/Valores Declarados e da Função

numero3 = 30

print("O resultado da Soma é:", numero3 + 15)

# Realizando Operações Logicas com print()

numero = 9

print(numero > 3)
print(numero < 10)
print(numero == 11)
print(numero >= 12)

# fstrings e Máscaras de substituiçãodentro da função print()

nome = "Fernando"

print(f"Seja muito bem-vindo, {nome}!")

# Operações dentro de fstrings

camisa = 19.90
calca = 39.90

print(f"A soma dos produtos é: R${(camisa+calca):.2f}")

# Sintaxe Antiga vs Atual 

nome = "Maria"

print("Bem-Vindo", nome, "!!!") # Antiga 1
print("Bem-Vindo"+ " " + nome + " ""!!!") # Antiga 2
print("Bem-Vindo %s !!!"%nome) # Antiga 3
print("Bem-Vindo {} !!!".format(nome)) # Antiga 4
print(f"Bem-Vindo {nome} !!!") # Atual
