from tkinter import *
from tkinter import messagebox

# MENU

def mostrarMsg():
    messagebox.showerror(title="Cadastros Ativados",message="Frame")
    

vmsg="Tipo de Alerta"

app = Tk()
app.title("Cadastro de Clientes - Ecommerce")
app.geometry("500x350")

vnum_txt=StringVar()

fr_quadro1=Frame(app,borderwidth=1,relief="solid")
fr_quadro1.place(x=10,y=10,width=300,height=100)

lb = Label(fr_quadro1,text="Tipo de Caixa (1, 2 ou 3)")
lb.place(x=10,y=10)
tb_num = Entry(fr_quadro1,textvariable=vnum_txt)
vnum_txt.set("1")
tb_num.place(x=10,y=30)

btn_msg = Button(fr_quadro1,text="Mostrar Mensagem",command=mostrarMsg)
btn_msg.place(x=10,y=60)

fr_quadro2=Frame(app,borderwidth=1,relief="solid",background="#008")
fr_quadro2.place(x=10,y=120,width=300,height=100)

lb_canal = Label(fr_quadro2,text="Curso",background="#008",foreground="#fff",font=("Arial",25))
lb_canal.pack(side=LEFT,fill=X,expand=True)

app.mainloop() 