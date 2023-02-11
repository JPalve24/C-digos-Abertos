import sqlite3
from sqlite3 import Error

#############CRIAR CONEXÃO####################
def ConexaoBanco():
    caminho="C:/Users/alves/OneDrive/Área de Trabalho/Udemy/SQL/Curso SQL/Bancos/agenda.db"
    con=None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


#############CRIAR TABELA####################
vcon = ConexaoBanco()

vsql="""CREATE TABLE tb_contatos(
        N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
        T_NOMECONTATO TEXT(30),
        T_TELEFONECONTATO TEXT(14),
        T_EMAILCONTATO TEXT(30)
    );"""

def CriarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as ex:
        print(ex)

CriarTabela(vcon,vsql)


vcon.close()          