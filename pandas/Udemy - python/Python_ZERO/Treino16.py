# Pilhas

sequencia = [11, 22, 33, 444]

pilha = []

for elemento in sequencia:
    pilha.append(elemento)

pilha.append(555)
pilha.pop()

while len(pilha) > 0:
    print(pilha)
    
    topo = pilha.pop()
    
    print(f"Objeto do topo da pilha: {topo}")
