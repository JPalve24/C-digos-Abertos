from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Cadastro de Clientes - Ecommerce")
app.geometry("500x350")

nb=ttk.Notebook(app)
nb.place(x=0,y=0,width=500,height=300)

tb1=Frame(nb)
tb2=Frame(nb)

nb.add(tb1,text="Cursos")
nb.add(tb2,text="Canal")

lb1=Label(tb1,text="Curso de Python")
lb2=Label(tb1,text="Curso de Java")
lb3=Label(tb2,text="Youtube.com")
lb4=Label(tb2,text="Google.com")

lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack()

app.mainloop() 