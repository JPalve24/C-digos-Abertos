from tkinter import *
import os

os.system("cls")

c=os.path.dirname(__file__)
nomeArquivo = c+"\\nomes.txt"

def gravarDados():
    arquivo = open(nomeArquivo,"a")
    arquivo.write("Nome......:%s"%vnome.get())
    arquivo.write("\nTelefone..:%s"%vtelefone.get())
    arquivo.write("\nEmail.....:%s"%vemail.get())
    arquivo.write("\nObservação:%s"%vobs.get("1.0",END))
    arquivo.write("\n\n")
    arquivo.close()

app = Tk()
app.title("CADASTRO DE CLIENTES")
app.geometry("500x350")
app.configure(background="#dde")

Label(app,text="Nome",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
vnome=Entry(app)
vnome.place(x=10,y=30,width=400,height=20)

Label(app,text="Telefone",background="#dde",foreground="#009",anchor=W).place(x=10,y=60,width=100,height=20)
vtelefone=Entry(app)
vtelefone.place(x=10,y=80,width=200,height=20)

Label(app,text="Email",background="#dde",foreground="#009",anchor=W).place(x=10,y=110,width=100,height=20)
vemail=Entry(app)
vemail.place(x=10,y=130,width=400,height=20)

Label(app,text="Obs.",background="#dde",foreground="#009",anchor=W).place(x=10,y=160,width=100,height=20)
vobs=Text(app)
vobs.place(x=10,y=180,width=200,height=100)

Button(app,text="Salvar",command=gravarDados).place(x=10,y=300,width=100,height=20)

app.mainloop() 
