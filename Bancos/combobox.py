from tkinter import *
from tkinter import ttk

def impEsporte():
    print(cb_esportes.get())

app = Tk()
app.title("Cadastro de Clientes - Ecommerce")
app.geometry("500x350")

listEsportes=["Futebol","Volei","Basket"]

lb_esporte=Label(app,text="Esportes")
lb_esporte.pack()

cb_esportes=ttk.Combobox(app,values=listEsportes,state="readonly")
cb_esportes.set("Futebol")
cb_esportes.pack()

btn_esportes=Button(app,text="Esporte Escolhido",command=impEsporte)
btn_esportes.pack()

app.mainloop() 