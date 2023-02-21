import sqlite3
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp+"\\contatos.db"

def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con


def dql(sql): #select
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(sql)
    res=c.fetchall()
    return res

def dml(sql): #insert, delete, update
    try:
        vcon=ConexaoBanco()
        c=vcon.cursor()
        c.execute(sql)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)