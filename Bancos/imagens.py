from tkinter import *
import os

# MENU

pastaApp=os.path.dirname(__file__)

app = Tk()
app.title("Cadastro de Clientes - Ecommerce")
app.geometry("500x350")

imgLogo=PhotoImage(file=pastaApp+"\\indice.gif")
l_logo=Label(app,image=imgLogo)
l_logo.place(x=10,y=10)

app.mainloop() 