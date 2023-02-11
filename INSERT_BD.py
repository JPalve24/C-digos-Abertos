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

vcon = ConexaoBanco()

nome = input("Nome: ")
telefone = input("Telefone: ")
email = input("Email: ")
vsql="INSERT INTO tb_contatos (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES('"+nome+"','"+telefone+"','"+email+"')"

def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro Inserido")
    except Error as ex:
        print(ex)

inserir(vcon,vsql)


vcon.close() 