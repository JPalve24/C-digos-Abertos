from tkinter import *

app = Tk()
app.title("SHOPEASE")
app.geometry("500x300")
app.configure(background="#dde")

txt1 = Label(app,text="Curso de Python",background="#008",foreground="#fff")
txt1.place(x=10,y=10,width=100,height=20)

vtxt="Módulo Tkinter"
vbg = "#ff0"
vfg = "#000"
txt2= Label(app,text=vtxt,background=vbg,foreground=vfg)
txt2.pack(ipadx=20,ipady=20,padx=5,pady=5,side="top",fill=Y,expand=True)

app.mainloop() 