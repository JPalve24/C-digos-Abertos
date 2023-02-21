from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco_2

def popular():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM tb_nomes ORDER BY ID"
    linhas=banco_2.dql(vquery)
    for i in linhas:
        tv.insert("","end",values=i)

def inserir():
    if vnome.get()=="" or vfone.get()=="":
        messagebox.showinfo(title="ERRO",message="Adicione os valores")
        return
    try:
        vquery = "INSERT INTO tb_nomes (nome,fone) VALUES ('"+vnome.get()+"','"+vfone.get()+"')"
        banco_2.dml(vquery)
    except:
        messagebox.showerror(title="ERRO",message="Erro ao Inserir")
        return
    popular()
    vnome.delete(0,END)
    vfone.delete(0,END)
    vnome.focus()

def deletar():
    vid=-1
    itemSelection=tv.selection()[0]
    valores=tv.item(itemSelection,"values")
    vid=valores[0]
    try:
        vquery = "DELETE FROM tb_nomes WHERE id="+vid
        banco_2.dml(vquery)
    except:
        messagebox.showwarning(title="ERRO",message="Erro ao deletar")
        return
    tv.delete(itemSelection)

def pesquisar():
    tv.delete(*tv.get_children())
    vquery="SELECT * FROM tb_nomes WHERE nome LIKE '%"+vnomepesquisar.get()+"%'"
    linhas=banco_2.dql(vquery)
    for i in linhas:
        tv.insert("","end",values=i)

app = Tk()
app.title("Cadastro de Clientes - Ecommerce")
app.geometry("600x450")

#####################################################

quadroGrid=LabelFrame(app,text="Contatos")
quadroGrid.pack(fill="both",expand="yes",padx=10,pady=10)

tv=ttk.Treeview(quadroGrid,columns=('id','nome','fone'),show='headings')
tv.column('id',minwidth=0,width=50)
tv.column('nome',minwidth=0,width=250)
tv.column('fone',minwidth=0,width=100)
tv.heading('id',text='ID')
tv.pack()
popular()

#####################################################

quadroInserir=LabelFrame(app,text="Inserir Novos Contatos")
quadroInserir.pack(fill="both",expand="yes",padx=10,pady=10)

lbnome=Label(quadroInserir,text="Nome")
lbnome.pack(side="left")
vnome=Entry(quadroInserir)
vnome.pack(side="left",padx=10)
lbfone=Label(quadroInserir,text="Fone")
lbfone.pack(side="left")
vfone=Entry(quadroInserir)
vfone.pack(side="left",padx=10)
btn_inserir = Button(quadroInserir,text="Inserir",command=inserir)
btn_inserir.pack(side="left",padx=10)

#####################################################

quadroPesquisar=LabelFrame(app,text="Pesquisar Contatos")
quadroPesquisar.pack(fill="both",expand="yes",padx=10,pady=10)

lbid=Label(quadroPesquisar,text="Nome")
lbid.pack(side="left")
vnomepesquisar=Entry(quadroPesquisar)
vnomepesquisar.pack(side="left",padx=10)
btn_pesquisar = Button(quadroPesquisar,text="Pesquisar",command=pesquisar)
btn_pesquisar.pack(side="left",padx=10)
btn_todos = Button(quadroPesquisar,text="Mostrar Todos",command=popular)
btn_todos.pack(side="left",padx=10)
btn_deletar = Button(quadroPesquisar,text="Deletar",command=deletar,background='red',foreground='white')
btn_deletar.pack(side="left",padx=10)

app.mainloop() 