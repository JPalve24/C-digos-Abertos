from tkinter import *

def futebolClicado():
    print(f"FUTEBOL: {vfut.get()}")

def voleiClicado():
    print(f"VOLEI: {vvol.get()}")

def basketClicado():
    print(f"BASKET: {vbask.get()}")

app = Tk()
app.title("Cadastro de Clientes - Ecommerce")
app.geometry("500x350")

vfut=IntVar()
vvol=IntVar()
vbask=IntVar()

fr_quadro1=Frame(app,borderwidth=1,relief="solid")
fr_quadro1.place(x=10,y=10,width=300,height=100)

cb_futebol=Checkbutton(fr_quadro1,text="Futebol",variable=vfut,onvalue=1,offvalue=0,command=futebolClicado)
cb_volei=Checkbutton(fr_quadro1,text="Volei",variable=vvol,onvalue=1,offvalue=0,command=voleiClicado)
cb_basket=Checkbutton(fr_quadro1,text="Basket",variable=vbask,onvalue=1,offvalue=0,command=basketClicado)

cb_futebol.pack(side=LEFT)
cb_volei.pack(side=LEFT)
cb_basket.pack(side=LEFT)



app.mainloop() 