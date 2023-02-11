from Treino23 import BaseDeDados

clientes = BaseDeDados()

clientes.inserir("Ana", 991358899)
clientes.inserir("Fernando", 981357239)
clientes.inserir("Maria", 964493779)

clientes.listar()

clientes.apagar("Ana")

clientes.listar()