# Try, Except

try:
    print(variavel)
except:
    pass

# Exibindo erro especifico

try:
    print(variavel)
except:
    print("A variavel não existe")
    
# qual erro aconteceu

try:
    print(a)
except NameError as erro:
    print("Ocorreu um erro: ", erro)

# Except genérico

except Exception as erro:
    print("Ocorreu um erro inesperado", erro)  