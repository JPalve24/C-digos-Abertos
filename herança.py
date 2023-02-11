class NPC:
    def __init__(self,nome,time,forca,municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100
    def info(self):
        print("Nome: "+self.nome)
        print("Time: "+str(self.time))
        print("Forca: "+str(self.forca))
        print("Municao: "+str(self.municao))
        print("Vivo: "+("sim" if self.vivo else "não"))
        print("Energia: "+str(self.energia))
        print("---------------------------------------")

class soldado(NPC):
    def __init__(self,nome,time):
        self.forca=200
        self.municao=200
        super().__init__(nome,time,self.forca,self.municao)

class guarda(NPC):
    def __init__(self,nome,time):
        self.forca=100
        self.municao=20
        super().__init__(nome,time,self.forca,self.municao)


class elite(NPC):
    def __init__(self,nome,time):
        self.forca=400
        self.municao=500
        super().__init__(nome,time,self.forca,self.municao)
    def inf(self):
        super().info()


s1=guarda("Olho",1)
s2=soldado("sold-04",2)
s3=elite("ninja",1)
s4=guarda("fedor",2)

s1.info()
s2.info()
s3.inf()
s4.info()