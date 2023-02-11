# Tamanho de uma String

frase1 = "Porto Alegre é uma cidade brasileira."

print(len(frase1))

# Contando desconciderando espaços e pontos

print(len(frase1) - frase1.count(" ") - frase1.count("."))

# Substituindo Elementos

frase1 = frase1.replace("Porto Alegre", "Banabuiú")

print(frase1)

# Contando elementos em uma string

print(frase1.count("a"))

# Posição de um elemento

print(frase1.find("é"))

# Leitura de caractere

print(frase1[3])
print(frase1[3:6])

# Desmembrando uma string

print(frase1.split())

# Concatenando strings

mensagem = "Seja bem-vinda "
usuario = "Ana Clara"

base = mensagem + usuario

print(base)

# Operadores Lógicos em String

aviso = "Não é permitida a entrada de menores de 18 anos"

print("anos" in aviso)
print("gestante" not in aviso)

# Maiusculo ou Minusculo

alerta = "Risco de Morte"

print(alerta.upper())
print(alerta.lower())

# Removendo Espaços de uma string

frase2 = "       olá senhor        "

print(frase2)
print(frase2.strip())

# Iniciais maiusculas

tema = "O diagnóstico por imagem como ferramenta de detecção de cancêr"

print(tema.title())

# Verificando se uma string é composta por letras e números

variavel = "aa44"

print(variavel.isalnum()) # algum caractere alfanumerico?
print(variavel.isalpha()) # Apenas letras?
print(variavel.isdigit()) # Apenas números?

# Trabalhando com intervalos de strings

print(frase1[25:32]) # Intervalo especifico
print(frase1[0:5]) # de inicio até posição
print(frase1[-9]) # de trás pra frente