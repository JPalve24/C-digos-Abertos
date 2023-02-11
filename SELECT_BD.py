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

vsql="SELECT * FROM tb_contatos WHERE N_IDCONTATO=2"

def consulta(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado

res = consulta(vcon,vsql)

for r in res:
    print(r)

vcon.close()