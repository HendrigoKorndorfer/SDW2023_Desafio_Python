import openai as openai
import pandas as pd

arquivo_origem = pd.read_csv(r'C:\Users\User\Downloads\SDW2023_Desafio.csv')

IDs_clientes = arquivo_origem['ID_cliente'].tolist()
nome_clientes = arquivo_origem['nome_cliente'].tolist()
valor_disponivel_clientes = arquivo_origem['valor_disponivel'].tolist()
perfis_clientes = arquivo_origem['perfil_cliente'].tolist()

#print(arquivo_origem)
print(IDs_clientes)
print(nome_clientes)
print(valor_disponivel_clientes)
print(perfis_clientes)

# Documentação Oficial da API OpenAI: https://platform.openai.com/docs/api-reference/introduction
# Informações sobre o Período Gratuito: https://help.openai.com/en/articles/4936830

# Para gerar uma API Key:
# 1. Crie uma conta na OpenAI
# 2. Acesse a seção "API Keys"
# 3. Clique em "Create API Key"
# Link direto: https://platform.openai.com/account/api-keys

openai_api_key = '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'
openai.api_key = openai_api_key

def generate_ai_news(nome_clientes, valor_disponivel_clientes, perfis_clientes):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em assessoria de investimentos financeiros."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem de recomendação de investimentos para {nome_clientes}, considerando que ela tem R${valor_disponivel_clientes} para investir e o perfil dela é {perfis_clientes} (máximo de 500 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for ID_cliente in IDs_clientes:
  recomendacao = generate_ai_news(nome_clientes, valor_disponivel_clientes, perfis_clientes)
  print(recomendacao)
  ID_cliente['recomendacao'].append({
      "description": recomendacao
  })