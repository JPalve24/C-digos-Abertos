# CONJUNTO NUMERICO

# Set

conjunto1 = {4, 10, 15, 20}

print(type(conjunto1))

# Operações com conjuntos númericos

cj1 = {1, 2, 3, 4, 5}
cj2 = {1, 3, 5, 7, 9}

print(cj2 - cj1) #Eliminar elementos comuns aos dois

# União de conjuntos

uniao = cj1.union(cj2)

print(uniao)

# Interseção de dois conjuntos

uniao = cj1.intersection(cj2)

print(uniao) # Os valores em comum

# Operadores Logicos

uniao = cj1.union(cj2)

print(uniao == cj1)
print(uniao >= cj2)

# Diferença entre conjuntos

c1 = {1, 2, 3, 4, 5} - {1, 2}

print(c1)




