import pandas as pd
import win32com.client as win32

#Importar base de dados

tabela_vendas = pd.read_excel("C:/Users/alves/OneDrive/Área de Trabalho/python/Curso hashtag/Vendas.xlsx")

#Visualizar base de dados

pd.set_option("display.max_columns",None)

#Faturamento por loja

Loja_Vendas = tabela_vendas[["ID Loja","Valor Final"]]

Fat_Loja = tabela_vendas.groupby("ID Loja").sum()

Fat_Loja_Val = tabela_vendas[["ID Loja","Valor Final"]].groupby("ID Loja").sum()


#Qtd de produtos vendidos por loja

Qtd_Loja = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()

#ticket médio por produto em cada loja

Ticket_med = (Fat_Loja_Val["Valor Final"]/Qtd_Loja["Quantidade"]).to_frame()
Ticket_med = Ticket_med.rename(columns={0:"Ticket Médio"})
print("-"*50)
print(Ticket_med)
print("-"*50)

#enviar email com relatório

outlook = win32.Dispatch("Outlook.application")
mail = outlook.CreateItem(0)
mail.To = "alvesjoaopaulo486@Gmail.com"
mail.Subject = "Relatório de Vendas por Loja"
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de vendas por cada loja.</p>

<p>Faturamento:</p>
{Fat_Loja_Val.to_html(formatters={"Valor Final": "R${:,.2f}".format})}

<p>Quantidade Vendida:</p>
{Qtd_Loja.to_html(formatters={"Quantidade": "{:,}".format})}

<p>Ticket Médio dos Produtos em Cada Loja:</p>
{Ticket_med.to_html(formatters={"Ticket Médio": "R${:,.2f}".format})}

<p>Qualquer Dúvida Estou a Disposição.</p>

<p>Att.,</p>
<p>João.ASN</p>
'''

mail.Send()

print("Email Enviado")