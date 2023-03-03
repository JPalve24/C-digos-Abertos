from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
import banco_2
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate,Image
import webbrowser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from tkcalendar import Calendar, DateEntry

# defs

def popular2():
    tv2.delete(*tv2.get_children())
    vquery = "SELECT * FROM tb_nomes ORDER BY ID"
    linhas=banco_2.dql(vquery)
    for i in linhas:
        tv2.insert("","end",values=i)

def buscar():
    tv2.delete(*tv2.get_children())
    vquery="SELECT * FROM tb_nomes WHERE nome LIKE '%"+nome_entry.get()+"%'"
    linhas=banco_2.dql(vquery)
    for i in linhas:
        tv2.insert("","end",values=i)

def printTudo():
    webbrowser.open("ListaGeral.pdf")

def imprimirTudo():
    valBarra(10000)
    try:
        vquery = "SELECT * FROM tb_nomes"
        linhas=banco_2.dql(vquery)
        cnv=canvas.Canvas("ListaGeral.pdf")
        cnv.setFont("Helvetica-Bold",24)
        cnv.drawString(200,790,'Cadastro de Clientes')
        
        cnv.setFont("Helvetica-Bold",12)
        cnv.drawString(40,740,'ID: ')
        cnv.drawString(70,740,'Nome: ')
        cnv.drawString(200,740,'Telefone: ')
        cnv.drawString(300,740,'UF: ')
        cnv.drawString(340,740,'Cidade: ')
        cnv.drawString(430,740,'Assinante: ')
        cnv.drawString(510,740,'Data: ')
        
        cnv.setFont("Helvetica",12)
        x = 40
        y = 700
        for i in linhas:
            id = i[0]
            nome = i[1]
            fone = i[2]
            estado= i[3]
            cidade = i[4]
            ass= i[5]
            data= i[6]
            cnv.drawString(x, y, str(id))
            cnv.drawString(x + 30, y, nome)
            cnv.drawString(x + 160, y, fone)
            cnv.drawString(x + 260, y, str(estado))
            cnv.drawString(x + 300, y, str(cidade))
            cnv.drawString(x + 420, y, str(ass))
            cnv.drawString(x + 470, y, str(data))
            y -= 20
        cnv.rect(20,720,550,3,fill=True,stroke=False)
        cnv.showPage()
        cnv.save()
        printTudo()
    except:
        messagebox.showerror(title="ERRO",message="Erro ao Gerar PDF")
        return
    var_barra.set(0)

def printCliente():
    webbrowser.open("cliente.pdf")

def geraRelatório():
    c=canvas.Canvas("cliente.pdf")
    codigo = codigo_entry.get()
    nome = nome_entry.get()
    telefone = telefone_entry.get()
    cidade = cidade_entry.get()
    estado = estado_entry.get()
    ass = text1.get()
    data = entry_data.get()
    c.setFont("Helvetica-Bold",24)
    c.drawString(200,790,'Ficha do Cliente')
    
    c.setFont("Helvetica-Bold",18)
    c.drawString(50,700,'ID: ')
    c.drawString(50,670,'Nome: ')
    c.drawString(50,640,'Telefone: ')
    c.drawString(50,610,'Cidade: ')
    c.drawString(50,580,'UF: ')
    c.drawString(50,540,'Assinante: ')
    c.drawString(50,500,'Data: ')
    
    c.setFont("Helvetica",18)
    c.drawString(150,700,codigo)
    c.drawString(150,670,nome)
    c.drawString(150,640,telefone)
    c.drawString(150,610,cidade)
    c.drawString(150,580,estado)
    c.drawString(150,540,ass)
    c.drawString(150,500,data)
    
    c.rect(20,470,550,5,fill=True,stroke=False)
    
    c.showPage()
    c.save()
    printCliente()

def valBarra(m):
    cont=0
    etapas=m/100
    while cont<etapas:
        cont+=10
        i=0
        while i<1000000:
            i+=1
        var_barra.set(cont)
        app.update()

def limpar():
    codigo_entry.delete(0,END)
    nome_entry.delete(0,END)
    telefone_entry.delete(0,END)
    cidade_entry.delete(0,END)
    estado_entry.set(" ")
    text1.set("Não")
    entry_data.delete(0,END)

def novo():
    if nome_entry.get()=="" or telefone_entry.get()=="" or estado_entry.get()==" " or cidade_entry.get()=="" or entry_data.get()=="":
        messagebox.showinfo(title="ERRO",message="Adicione os valores")
        return
    try:
        vquery = "INSERT INTO tb_nomes (nome,fone,Estado,Cidade,assinante,data) VALUES ('"+nome_entry.get()+"','"+telefone_entry.get()+"','"+estado_entry.get()+"','"+cidade_entry.get()+"','"+text1.get()+"','"+entry_data.get()+"')"
        banco_2.dml(vquery)
    except:
        messagebox.showerror(title="ERRO",message="Erro ao Inserir")
        return
    popular2()
    limpar()
    nome_entry.focus()

def duploClick(event):
    limpar()
    tv2.selection()
    for i in tv2.selection():
        col1,col2,col3,col4,col5,col6,col7=tv2.item(i,'values')
        codigo_entry.insert(END,col1)
        nome_entry.insert(END,col2)
        telefone_entry.insert(END,col3)
        estado_entry.set(col4)
        cidade_entry.insert(END,col5)
        text1.set(col6)
        entry_data.insert(END,col7)

def apagar():
    codigo = codigo_entry.get() 
    vid=-1
    itemSelection=tv2.selection()[0]
    valores=tv2.item(itemSelection,"values")
    vid=valores[0]
    try:
        vquery = "DELETE FROM tb_nomes WHERE id="+vid
        banco_2.dml(vquery)
        messagebox.showinfo(title="SUCESSO",message="Valores deletados!")
    except:
        messagebox.showwarning(title="ERRO",message="Erro ao deletar")
        return
    tv2.delete(itemSelection)

def alterar():
    codigo = codigo_entry.get()
    nome = nome_entry.get()  
    telefone = telefone_entry.get()
    estado = estado_entry.get()
    cidade=cidade_entry.get()
    ass = text1.get()
    data = entry_data.get()
    vid=-1
    itemSelection=tv2.selection()[0]
    valores=tv2.item(itemSelection,"values")
    vid=valores[0]
    try:
        vquery = "UPDATE tb_nomes SET nome = '"+nome+"', fone = '"+telefone+"',Estado = '"+estado+"', Cidade = '"+cidade+"', assinante = '"+ass+"', data = '"+data+"' WHERE id="+vid
        banco_2.dml(vquery)
        messagebox.showinfo(title="SUCESSO",message="Valores alterados!")
    except:
        messagebox.showerror(title="ERRO",message="Erro ao alterar")
        return
    popular2()
    limpar()

def Menus():
    menubar = Menu(app,tearoff=0)
    app.config(menu=menubar)
    filemenu=Menu(menubar,tearoff=0)
    filemenu2=Menu(menubar,tearoff=0)
    
    def quit(): app.destroy()
    
    menubar.add_cascade(label= "Opções",menu=filemenu)
    menubar.add_cascade(label= "Sobre",menu=filemenu2)
    
    filemenu.add_command(label="Sair",command=quit)
    filemenu.add_command(label="Imprimir Dados",command=imprimirTudo)
    filemenu.add_command(label="Ficha do Cliente",command=geraRelatório)
    filemenu2.add_command(label="Info.")

def dashboard():
    #dashboard

    lb_dash = Label(frame_3,text="Relatório Geral",fg ='black',font=('verdana',12,'bold'))
    lb_dash.place(relx=0,rely=0)

    # clientes

    cont = "SELECT COUNT(nome) FROM tb_nomes"
    valor1=banco_2.dql(cont)

    frame_cl = Frame(frame_3,bd=4,background='white')
    frame_cl.place(relx=0,rely=0.08,relwidth=0.3,relheight=0.2)
    lb_cl = Label(frame_cl,text="Número de Clientes",fg ='black',font=('verdana',8,'bold'),background='white')
    lb_cl.place(relx=0.1,rely=0)
    frame_qcl = Frame(frame_cl,background='blue')
    frame_qcl.place(relx=0,rely=0,relwidth=0.05,relheight=0.25)
    lb_cl_valor = Label(frame_cl,text=str(valor1[0][0])+" Clientes",fg ='blue',font=('verdana',10,'bold'),background='white')
    lb_cl_valor.place(relx=0.25,rely=0.5)

    # assinantes

    cont_ass = "SELECT COUNT(nome) FROM tb_nomes WHERE assinante = 'Sim'"
    valor2=banco_2.dql(cont_ass)

    frame_ass = Frame(frame_3,bd=4,background='white')
    frame_ass.place(relx=0.31,rely=0.08,relwidth=0.3,relheight=0.2)
    lb_ass = Label(frame_ass,text="Número Assinantes",fg ='black',font=('verdana',8,'bold'),background='white')
    lb_ass.place(relx=0.1,rely=0)
    frame_qass = Frame(frame_ass,background='blue')
    frame_qass.place(relx=0,rely=0,relwidth=0.05,relheight=0.25)
    lb_ass_valor = Label(frame_ass,text=str(valor2[0][0])+" Assinantes",fg ='blue',font=('verdana',10,'bold'),background='white')
    lb_ass_valor.place(relx=0.25,rely=0.5)

    # clientes/ UF

    uf = "SELECT COUNT(nome),Estado FROM tb_nomes GROUP BY Estado"
    valor3=banco_2.dql(uf)

    frame_uf = Frame(frame_3,bd=4,background='white')
    frame_uf.place(relx=0,rely=0.30,relwidth=1,relheight=0.6)
    lb_uf = Label(frame_uf,text="Clientes / UF",fg ='black',font=('verdana',8,'bold'),background='white')
    lb_uf.place(relx=0.05,rely=0)
    frame_quf = Frame(frame_uf,background='blue')
    frame_quf.place(relx=0,rely=0,relwidth=0.02,relheight=0.13)

    list_est = []
    list_nome = []
    for i in valor3:
        list_nome.append(i[0])
        list_est.append(i[1])

    figura = plt.Figure(figsize=(10, 2.5),dpi=60)
    ax=figura.add_subplot(111)

    ax.bar(list_est,list_nome)
    totals=[]
    c=0
    for i in ax.patches:
        ax.text(i.get_x()+.4,i.get_height()+.05,str(list_nome[c]),fontsize=12,fontstyle='italic',verticalalignment='baseline',color='black')
        c+=1

    ax.patch.set_facecolor('#FFFFFF')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False,left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True,color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura,frame_uf)
    canva.get_tk_widget().place(relx=0,rely=0.20)

def calendario():
    def print_cal():
        dataIni = calendario1.get_date()
        calendario1.destroy()
        entry_data.delete(0,END)
        entry_data.insert(END,dataIni)
        calData.destroy()

    
    calendario1 = Calendar(frame_1,fg="gray75",bg="blue",font=("Times",'9','bold'),locale='pt_br')
    calendario1.place(relx=0.4,rely=0.1)
    calData = Button(frame_1,text="Inserir Data",command=print_cal)
    calData.place(relx=0.55,rely=0.85,height=25,width=100)

# INTERFACE INICIAL

pastaApp = os.path.dirname(__file__)

app = tix.Tk()
app.title("Sistema de Cadastros")
app.geometry("700x500")
app.resizable(True,True)
app.maxsize(width=900,height=700)
app.minsize(width=500,height=400)

# ABAS 

nb=ttk.Notebook(app)
nb.place(relx=0,rely=0,relwidth=1,relheight=1)

tb1=Frame(nb,background="#dde")
tb2=Frame(nb,background="#dde")

nb.add(tb1,text="Cadastro")
nb.add(tb2,text="Relatório")

# Frames Cadastro
frame_1 = Frame(tb1,bd=4,highlightbackground='black',highlightthickness=3,bg='#99ABB5')
frame_1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.46)

frame_2 = Frame(tb1,bd=4,highlightbackground='black',highlightthickness=3)
frame_2.place(relx=0.02,rely=0.5,relwidth=0.96,relheight=0.46)

frame_3 = Frame(tb2,bd=4,highlightbackground='black',highlightthickness=3)
frame_3.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.8)

Menus()

# Progress bar
var_barra=DoubleVar()
var_barra.set(0)

pb=ttk.Progressbar(tb1,variable=var_barra,maximum=100)
pb.place(x=0,y=0,relwidth=1,height=5)


# Botões
canvas_bt = Canvas(frame_1,bd=0,bg='#1e3743',highlightbackground='gray',highlightthickness=5)
canvas_bt.place(relx=0.19,rely=0.08,relwidth=0.22,relheight=0.19)

bt_limpar = Button(frame_1,text="Limpar", bd=2,bg='#107db2',activebackground='#108ecb',activeforeground='white',fg='white',font=('verdana',8,'bold'),command=limpar)
bt_limpar.place(relx=0.2,rely=0.1,relwidth=0.1,relheight=0.15)
bt_buscar = Button(frame_1,text="Buscar", bd=2,bg='#107db2',activebackground='#108ecb',activeforeground='white',fg='white',font=('verdana',8,'bold'),command=buscar)
bt_buscar.place(relx=0.3,rely=0.1,relwidth=0.1,relheight=0.15)

canvas_bt2 = Canvas(frame_1,bd=0,bg='#1e3743',highlightbackground='gray',highlightthickness=5)
canvas_bt2.place(relx=0.59,rely=0.08,relwidth=0.32,relheight=0.19)

bt_novo = Button(frame_1,text="Novo", bd=2,bg='#107db2',activebackground='#108ecb',activeforeground='white',fg='white',font=('verdana',8,'bold'),command=novo)
bt_novo.place(relx=0.6,rely=0.1,relwidth=0.1,relheight=0.15)
bt_alterar = Button(frame_1,text="Alterar", bd=2,bg='#107db2',activebackground='#108ecb',activeforeground='white',fg='white',font=('verdana',8,'bold'),command=alterar)
bt_alterar.place(relx=0.7,rely=0.1,relwidth=0.1,relheight=0.15)
bt_apagar = Button(frame_1,text="Apagar", bd=2,bg='#107db2',activebackground='#108ecb',activeforeground='white',fg='white',font=('verdana',8,'bold'),command=apagar)
bt_apagar.place(relx=0.8,rely=0.1,relwidth=0.1,relheight=0.15)

#Calendario

bt_calendario = Button(frame_1,text="Data",fg="blue",font=('verdana',8,'bold'),command=calendario)
bt_calendario.place(relx=0.05,rely=0.87,relwidth=0.08,relheight=0.1)
entry_data = Entry(frame_1,width=10)
entry_data.place(relx=0.14,rely=0.87,relwidth=0.1,relheight=0.1)


#balloons

balao_limpar = tix.Balloon(frame_1)
balao_limpar.bind_widget(bt_limpar,balloonmsg="Limpar todos as caixas de texto")
balao_buscar = tix.Balloon(frame_1)
balao_buscar.bind_widget(bt_buscar,balloonmsg="Filtra a tabela com os valores da entrada 'Nome'")
balao_novo = tix.Balloon(frame_1)
balao_novo.bind_widget(bt_novo,balloonmsg="Adiciona os valores digitados ao banco de dados")
balao_alterar = tix.Balloon(frame_1)
balao_alterar .bind_widget(bt_alterar,balloonmsg="Edita os valores de cadastro do cliente selecionado")
balao_apagar = tix.Balloon(frame_1)
balao_apagar .bind_widget(bt_apagar,balloonmsg="Deleta o cliente selecionado do banco de dados")

# Labels e Entrys

dashboard()


# codigo
lb_codigo = Label(frame_1,text="Código",fg='darkblue',bg='#99ABB5')
lb_codigo.place(relx=0.05,rely=0.05)

codigo_entry = Entry(frame_1)
codigo_entry.place(relx=0.05,rely=0.15,relwidth=0.08)

# nome

lb_nome = Label(frame_1,text="Nome",fg='darkblue',bg='#99ABB5')
lb_nome.place(relx=0.05,rely=0.35)

nome_entry = Entry(frame_1)
nome_entry.place(relx=0.05,rely=0.45,relwidth=0.5)

# telefone

lb_telefone = Label(frame_1,text="Telefone",fg='darkblue',bg='#99ABB5')
lb_telefone.place(relx=0.05,rely=0.6)

telefone_entry = Entry(frame_1)
telefone_entry.place(relx=0.05,rely=0.7,relwidth=0.2)

# cidade

lb_cidade = Label(frame_1,text="Cidade",fg='darkblue',bg='#99ABB5')
lb_cidade.place(relx=0.45,rely=0.60)

cidade_entry = Entry(frame_1)
cidade_entry.place(relx=0.45,rely=0.7,relwidth=0.3)

# estado

listEstados=[" ","AC","AL","AM","AP","BA","CE","DF","ES","GO","MA","MG","MS","MT","PA","PB","PE","PI","PR","RJ","RN","RO","RR","RS","SC","SE","SP","TO"]

lb_estado = Label(frame_1,text="Estado",fg='darkblue',bg='#99ABB5')
lb_estado.place(relx=0.3,rely=0.60)

estado_entry=ttk.Combobox(frame_1,values=listEstados,state="readonly")
estado_entry.set(" ")
estado_entry.place(relx=0.3,rely=0.7,relwidth=0.1)

# assinante

vass=IntVar()

lb_ass = Label(frame_1,text="Assinante?",fg='darkblue',bg='#99ABB5')
lb_ass.place(relx=0.64,rely=0.35)

text1 = StringVar()

text1.set('Não')

cb_assin=Checkbutton(frame_1, textvariable = text1, variable = text1,
                          offvalue = 'Não',
                          onvalue = 'Sim',bg='#99ABB5')
cb_assin.place(relx=0.64,rely=0.45)


# treeview Cadastro
tv2=ttk.Treeview(frame_2,columns=('id','nome','fone','estado','cidade','assinante','data'),show='headings',height=10)
tv2.column('id',minwidth=0,width=30)
tv2.column('nome',minwidth=0,width=100)
tv2.column('fone',minwidth=0,width=115)
tv2.column('estado',minwidth=0,width=50)
tv2.column('cidade',minwidth=0,width=80)
tv2.column('assinante',minwidth=0,width=20)
tv2.column('data',minwidth=0,width=40)
tv2.heading('id',text='ID')
tv2.heading('nome',text='Nome')
tv2.heading('fone',text='Telefone')
tv2.heading('estado',text='Estado')
tv2.heading('cidade',text='Cidade')
tv2.heading('assinante',text='Ass.')
tv2.heading('data',text='Data')
tv2.place(relx=0.01,rely=0.01,relwidth=0.95,relheight=0.98)
scroll = Scrollbar(frame_2,orient='vertical')
tv2.configure(yscroll=scroll.set)
scroll.place(relx=0.96,rely=0.01,relwidth=0.04,relheight=0.98)
popular2()
tv2.bind("<Double-1>",duploClick)

# FIM
app.mainloop() 