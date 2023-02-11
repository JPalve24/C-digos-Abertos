# Arredondando casas

equacao = ((50 + 25) * 7.2) / 3.8

print(f"O resultado bruto da equação é {equacao}")

print(f"O resultado é {equacao:.2f}")

print(f"O resultado da equação é {round(equacao, 3)}")

# Igualdade

print(5 == 6)

print(12 == 12)

# Diferença

print(5 != 12)

# OPERADORES LOGICOS COMPOSTOS
# Todas as condições precisam ser verdadeiras

print(7 != 3 and 2 > 3)

# Operador de membro IS

num1, num2, num3 = 4, 9, 9

print(num1 == num2)
print(num1 is num2)

print(num2 is 9)
print(num2 is num3)

# Operador de membro IN

lista = [1, 2, 3, "Ana", "Maria"]

print(2 in lista)
print("A" in lista)
print("A" in lista[3])

# Negação logica

print(7 not in lista)

# Maior que

print(10 > 4)

# Menor que

print(10 < 4)

# Maior igual

print(7 > 4)

# Menor igual

print(10 < 12)

# Operações compostas

x, y = 2, 7

print(x is not 2 and y != x)

# Operadores de identidade e OR

alugel, energia, agua = 250, 250, 65

print(alugel is energia)
print(alugel is agua or agua is energia)