import re

texto = "Curso de python da porra la do youtube porra"
res = re.findall("o",texto)
print(res)

###############################

res = re.search("porra",texto)
print(res.start())
print(res.end())
print(res.end()-res.start())

##############################

res = re.split(" ",texto)
print(res)


##############################
res = re.sub(" ",".",texto)
print(res)