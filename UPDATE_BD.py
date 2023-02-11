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

vsql="UPDATE tb_contatos SET T_NOMECONTATO = 'Bruno' WHERE N_IDCONTATO=1"

def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro Atualizado")

atualizar(vcon,vsql)

vcon.close() 