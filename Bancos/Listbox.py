from tkinter import *

def impEsporte():
    print(lb_esportes.get(ACTIVE))

def insEsporte():
    lb_esportes.insert(END,vnovo_esporte.get())

app = Tk()
app.title("Cadastro de Clientes - Ecommerce")
app.geometry("500x350")

listEsportes=["Futebol","Volei","Basket"]

lb_esportes=Listbox(app)
for esportes in listEsportes:
    lb_esportes.insert(END,esportes)
lb_esportes.pack()

btn_esporte=Button(app,text="Imprimir Esporte",command=impEsporte)
btn_esporte.pack()

vnovo_esporte = Entry(app)
vnovo_esporte.pack()

btn_inserir=Button(app,text="Inserir Esporte",command=insEsporte)
btn_inserir.pack()

app.mainloop() 