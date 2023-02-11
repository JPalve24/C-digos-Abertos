# Laço For

print("="*100)
nome = "Alberto"

for i in nome:
    print(i)
    
print("="*100)

# Laço For em um intervalo

for i in range(0, 11):
    print(i)
    
print("="*100)

# Laço For Retornando Dados Para Uma Variavel

vendas, total = [1000, 459, 911, 200, 838, 50], 0

for i in vendas:
    total += i
    
print(total)

print("="*100)

# Intervalo Personalizado

for i in range(0, 11, 2):
    print(i)
    
print("="*100)

# Ordem inversa

for i in range(10, 0, -1):
    print(i)
    
print("="*100)

# Laço interagindo com usuario

num = int(input("Digite um número limite: "))

for i in range(0, num + 1):
    print(i)
    
print("="*100)

# Laço retornando tamanho de uma variavel

nome, num = "Fernando", 0

for num in range(len(nome)):
    print(num)



