# LISTAS

# Lista e indices

lista1 = ["Ana clara", "Carlos", "Michele", "Fernando", 1987]

print(lista1[3])
print(lista1[3][3])

# Descobrindo o indice de um dado na lista

print(lista1.index("Michele"))

# Qtd de elementos na lista

print(len(lista1))

# Adicionar ao fim da lista

lista1.append("Paulo")
lista1.append(9999)

print(lista1)

# Substituir elementos

lista1[2] = "José"
lista1[6] = 2

print(lista1)

# Novo elemento na lista

lista1.insert(2, "João")

print(lista1)

# Remover elemento

lista1.remove(lista1[5])

print(lista1)

# Lista dentro de lista

cadastro = [1, 2, 3, 4, ["Ana", "Maria", "Paulo", "Roberto"]]

print(cadastro[4])

# Laço de repetição For dentro de lista

repetir = "s"
fatura = []
total = 0

while repetir == "s":
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    
    fatura.append([produto, preco])
    total += preco
    
    repetir = input("Deseja continuar? (S ou N) ").lower()

for i in fatura:
    print(i[0], ":", i[1])
    
print(f"O total da fatura é R$ {total:,.2f}")
