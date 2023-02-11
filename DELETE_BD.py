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


#############DELETAR####################

vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO=2"

def deletar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro Removido")

deletar(vcon,vsql)

vcon.close() 