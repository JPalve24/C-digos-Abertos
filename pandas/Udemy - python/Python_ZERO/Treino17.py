# DICIONARIOS

# Sintaxe

dicionario = {"Chave": "Valor"}

print(dicionario)

# adicionar elementos

dic1 = {"Nome1": "Paulo"}

dic1["Nome2"] = "Veronica"

print(dic1)

# Alterando o valor de uma chave 

dicionario1 = {"Nome1": "Ana",
               "Nome2": "Carla",
               "Nome3": "Maria"}

dicionario1["Nome2"] = "Barbara"

print(dicionario1)

# Acessando elemento

dicionario1 = {"Nome": "Fernando",
               "Idade": 32,
               "Sexo": "Masculino",
               "Nacionalidade": "Brasileiro"}

print(dicionario1["Nome"])
print(dicionario1["Nacionalidade"])

# Construtor de dicionarios

dicionario2 = dict(chave1 = "Valor da chave 1",
                   chave2 = "valor da chave 2")

print(dicionario2)
print(type(dicionario2))

# Consultando as chaves

print(dicionario2.keys())

# Consultando os valores

print(dicionario2.values())

# Pesquisando pela chave, obtendo valor

d3 = {
    "1": "Ana",
    "2": "Maria",
    "3": "Paulo",
    "4": "Marcos"
}

print(d3.get("5"))
print(d3.get("2"))

# Pesquisando via operador logico

print("3" in d3)

# Buscando elemento especifico via operador logico

print(d3["2"] == "Maria")

# Atualizando um elemento 

d4 = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D"
}

d4.update({"2" : "E"})

print(d4)

# Remover elemento

d4 = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D"
}

del d4["4"]

print(d4)

# Tamanho do dicionario

print(len(d4))
print(len(d4["1"]))

# For nas chaves e valores

for chaves in d4.keys(): # Só chaves
    print("Chaves: ", chaves)
    
for valores in d4.values(): # Só valores
    print("Valores: ", valores)
    
for chaves in d4.keys(): # Ambos
    for valores in d4[chaves]:
        print(f"Chave: {chaves} - Valor: {valores}")
  
# Outra forma para Ambos

for itens in d4.items():
    print("Chaves : Valores = ", itens)
 
# Mais uma forma:

for n, o in d4.items():
     print(f"Chave {n} : Valor {o} ")
     
# Lista em Dicionarios

dict = {"almox": ["Folha de Oficio", "Caneta", "Grampeador"],
        "Cozinha": ["Café", "Açucar"]}

print(dict["almox"][0])
print(dict["Cozinha"][1])

# Remover elementos por POP()

dicionario1 = {"Nome": "Fernando",
               "Idade": 32,
               "Sexo": "Masculino",
               "Nacionalidade": "Brasileiro"}

r = dicionario1.pop("Nacionalidade") # Mesmo que 'del'

print(r)

# Dicionario em dicionarios

usuarios = {
    "João":{
        "Identificador":"0001",
        "Cargo": "Porteiro",
        "Salario": "2000"
    },
    "Maria":{
        "Identificador":"0003",
        "Cargo": "Aux. Limpeza",
        "Salario": "1900"
    },
    "José":{
        "Identificador":"0002",
        "Cargo": "Técnico",
        "Salario": "2500"
    }
}

for chaves, valores in usuarios.items():
    print(f"Funcionário: {chaves}")
    
    for i, j in valores.items():
        print(f"\t {i} = {j}")