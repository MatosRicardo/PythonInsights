# Passo 1: Importar a base de dados
import pandas as pd

# Carregando a base de dados de cancelamentos
tabela = pd.read_csv("cancelamentos_sample.csv")


# Passo 2: Visualizar a base de dados (entender a base + identificar problemas)

# Removendo a coluna "CustomerID" que não será utilizada
tabela = tabela.drop(columns="CustomerID")
print(tabela)  # Exibe a tabela para análise


# Passo 3: Corrigir os problemas da base de dados (tratamento de dados)

# Exibe informações da tabela para identificar dados faltantes
print(tabela.info())  

# Remove as linhas com valores nulos
tabela = tabela.dropna()


# Passo 4: Análise Inicial -> quantos clientes cancelaram e qual a % de clientes
# Contar na coluna cancelou os valores
print(tabela["cancelou"].value_counts())

# percentual de cancelamento
print(tabela["cancelou"].value_counts(normalize=True))


# Passo 5: Análise de causa de cancelamento de clientes
# (Comparar as outras colunas da tabela com a coluna de cancelamento)
import plotly.express as px


# criar o gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou", text_auto=True)
    #exibir o gráfico
    grafico.show()
    
    
# Usuários do contrato mensal sempre cancelam
  # Evitar o contrato mensal e incentivar (com desconto) os contratos anuais e trimestrais
  
# Todos os usuários que ligarem mais de 4x para o call center, cancelaram o serviço
  # Criar um processo que quando um usuário bateu 3 ligações para o call center, alerta vermelho
  
# Usuários que atrasam o pagamento pra mais de 20 dias cancelam o produto
  # Criar um alerta para quando o atraso do pagamento bater 15 dias, entrar em contato
  
# Duracao_contrato -> diferente do mensal

condicao = tabela["duracao_contrato"] != "Monthly"
tabela = tabela[condicao]
 
# ligacoes_callcenter -> menor ou igual a 4
condicao = tabela["ligacoes_callcenter"] <= 4
tabela = tabela[condicao]

# atraso_pagamento <= 20 dias
condicao = tabela["dias_atraso"] <= 20
tabela = tabela[condicao]

# Percentual
print(tabela["cancelou"].value_counts(normalize=True))