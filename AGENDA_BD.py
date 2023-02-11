import os
import sqlite3
from sqlite3 import Error

## Conexão Banco ##

def ConexaoBanco():
    caminho= "SQL/Curso SQL/Bancos/agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação Realizada com sucesso")
        #conexao.close()

def consultar(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    res=c.fetchall()
    return res


def MenuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro por ID")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")

def Inserir():
    os.system("cls")
    nome=input("Digite o Nome: ")
    telefone=input("Digite o Telefone: ")
    email=input("Digite o Email: ")
    vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('"+nome+"','"+telefone+"','"+email+"')"
    query(vcon,vsql)

def Atualizar():
    os.system("cls")
    vid=input("Digite o ID do Registro a ser Alterado: ")
    r=consultar(vcon,"SELECT * FROM tb_contatos WHERE N_IDCONTATO="+vid)
    rnome=r[0][1]
    rtelefone=r[0][2]
    remail=r[0][3]
    vnome=input("Digite o Nome: ")
    vtelefone=input("Digite o Telefone: ")
    vemail=input("Digite o Email: ")
    if(len(vnome)==0):
        vnome=rnome
    if(len(vtelefone)==0):
        vtelefone=rtelefone
    if(len(vemail)==0):
        vemail=remail
    vsql="UPDATE tb_contatos SET T_NOMECONTATO='"+vnome+"', T_TELEFONECONTATO='"+vtelefone+"', T_EMAILCONTATO='"+vemail+"' WHERE N_IDCONTATO="+vid
    query(vcon,vsql)

def Deletar():
    os.system("cls")
    vid=input("Digite o ID do Registro a ser Deletado: ")
    vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO="+vid
    query(vcon,vsql)
    
def ConsultarId():
    vsql="SELECT * FROM tb_contatos"
    res=consultar(vcon,vsql)
    vlim=10
    vcont=0
    for r in res:
        print("ID:{0:_<3} Nome:{1:_<30} Telefone:{2:_<14} Email:{3:_<30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1
        if vcont>=vlim:
            vcont=0
            os.system("pause")
            os.system("cls")
    print("Fim da Lista")
    os.system("pause")        
    
def ConsultarNome():
    vnome = input("Digite o Nome: ")   
    vsql="SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%"+vnome+"%'"
    res=consultar(vcon,vsql)
    vlim=10
    vcont=0
    for r in res:
        print("ID:{0:_<3} Nome:{1:_<30} Telefone:{2:_<14} Email:{3:_<30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1
        if vcont>=vlim:
            vcont=0
            os.system("pause")
            os.system("cls")
    print("Fim da Lista")
    os.system("pause") 

opc=0
while opc!=6:
    MenuPrincipal()
    opc=int(input("Digite uma Opção: "))
    if opc==1:
        # INSERIR #
        Inserir()
    elif opc==2:
        # DELETAR #
        Deletar()
    elif opc==3:
        # ATUALIZAR # 
        Atualizar()
    elif opc==4:
        # CONSULTAR ID # 
        ConsultarId()
    elif opc==5:
        # CONSULTAR NOME #
        ConsultarNome()
    elif opc==6:
        os.system("cls")
        print("Programa Finalizado")
    else:
        os.system("cls")
        print("Opção Inválida")
        os.system("pause")

vcon.close()
os.system("pause")
