import pandas as pd
from twilio.rest import Client


account_sid = "AC5c96e44d3a9cf84365184ed1b0af532f"
auth_token = "87550f4a5227726d606451dc030e63f7"
client = Client(account_sid, auth_token)

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"archives/{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês de {mes} alguem bateu a meta, vendedor: {vendedor}, vendas: {vendas}.")
        message = client.messages.create(
            body= "TESTE",
            from_='+18045701798',
            to='+5543999223399'
        )
        print(message.sid)