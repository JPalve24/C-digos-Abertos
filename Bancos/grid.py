from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Cadastro de Clientes - Ecommerce")
app.geometry("500x350")

lb1=Label(app,text="Canal")
lb2=Label(app,text="Digite seu Nome")
lb3=Label(app,text="Informe sua Idade")

et_nome=Entry(app)
et_idade=Entry(app)

btn=Button(app,text="Imprimir")

lb1.grid(column=0,row=0, columnspan=2,pady=15)

lb2.grid(column=0,row=1,sticky="w",padx=5,pady=1)
et_nome.grid(column=0,row=2,padx=5,pady=5)

lb3.grid(column=1,row=1,sticky="w",padx=5,pady=1)
et_idade.grid(column=1,row=2,padx=5,pady=5)

btn.grid(column=0,row=5, columnspan=2,pady=5)

app.mainloop() 