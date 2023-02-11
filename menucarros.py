import os
carros=[]

class Carro:
    nome=""
    pot=0
    velMax=0
    ligado=False
    def __init__(self,nome,pot):
        self.nome=nome
        self.pot=pot
        self.velMax=int(pot)*2
    def ligar(self):
        self.ligado=True
    
    def desligar(self):
        self.ligado=False
    
    def info(self):
        print("Nome..."+self.nome)
        print("Potencia..."+str(self.pot))
        print("Velocidade Maxima..."+str(self.velMax))
        print("Status..."+("Ligado" if self.ligado==True else "Desligado"))

def Menu():
    os.system("cls") or None
    print("1 - Novo Carro")
    print("2 - Informacoes do Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carros")
    print("7 - Sair")
    print("Quantidade de Carros: " + str(len(carros)))
    opc=input("Digite uma Opcao: ")
    return opc

def NovoCarro():
    os.system("cls") or None
    n=input("Nome do Carro: ")
    p=input("Potencia do Carro: ")
    carro=Carro(n,p)
    carros.append(carro)
    print("Novo Carro Criado!!!")
    os.system("pause")

def informacoes():
    os.system("cls") or None
    n=input("Informe o numero do carro que deseja ver: ")
    try:
        carros[int(n)].info()
    except:
        print("Carro Nao Existe")
    os.system("pause")

def ExcluirCarro():
    os.system("cls") or None
    n=input("Informe o numero do carro que deseja excluir: ")
    try:
        del carros[int(n)]
    except:
        print("Carro Nao Existe")
    os.system("pause")

def LigarCarro():
    os.system("cls") or None
    n=input("Informe o numero do carro que deseja ligar: ")
    try:
        carros[int(n)].ligar()
        print("Carro Ligado")
    except:
        print("Carro Nao Existe")
    os.system("pause")

def DesligarCarro():
    os.system("cls") or None
    n=input("Informe o numero do carro que deseja desligar: ")
    try:
        carros[int(n)].desligar()
        print("Carro Desligado")
    except:
        print("Carro Nao Existe")
    os.system("pause")

def ListarCarro():
    os.system("cls") or None
    p=0
    for c in carros:
        print(str(p) + "-" + c.nome)
        p=p+1
    os.system("pause")


ret=Menu()
while ret < "7":
    if ret=="1":
        NovoCarro()
    elif ret =="2":
        informacoes()
    elif ret == "3":
        ExcluirCarro()
    elif ret =="4":
        LigarCarro()
    elif ret == "5":
        DesligarCarro()
    elif ret =="6":
        ListarCarro()
    ret=Menu()

os.system("cls") or None
print("Programa Finalizado")