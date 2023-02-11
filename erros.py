try:
    print("d")

except NameError:
    print("Valor nao definido")

except:
    print("Erro desconhecido")

else:
    print("Tudo certo")
    
finally:
    print("Fim do Programa")


num = -1

if num < 1:
    raise Exception("Valor nao permitido")