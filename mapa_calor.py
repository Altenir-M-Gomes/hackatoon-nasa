import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Início do Script Principal ---

# Etapa 2: Carregar e preparar os dados
try:
    df = pd.read_csv('dados_nasa.csv')
except FileNotFoundError:
    print("Erro: O arquivo 'dados_temperatura.csv' não foi encontrado.")
    print("Certifique-se de que o arquivo está no mesmo diretório que o script.")
    exit()

# IMPORTANTE: Um mapa de calor funciona melhor com dados de um único período.
# Se seu CSV tiver vários meses, filtre para o mês que deseja visualizar.
# Vamos usar o primeiro mês que aparecer no arquivo.
mes_para_visualizar = df['year_month'].unique()[0]
df_filtrado = df[df['year_month'] == mes_para_visualizar]

print(f"Gerando mapa de calor para o período: {mes_para_visualizar}")

# Etapa 3: "Pivotar" os dados para criar uma grade (matriz)
# As linhas (index) serão a latitude, as colunas a longitude, e os valores a temperatura T2M.
heatmap_data = df_filtrado.pivot_table(index='latitude', columns='longitude', values='T2M')

# Etapa 4: Gerar o mapa de calor
plt.figure(figsize=(12, 8)) # Define o tamanho da figura para melhor visualização

# cmap='RdYlGn_r' é o mapa de cores Red-Yellow-Green (Vermelho-Amarelo-Verde) invertido.
# A inversão ('_r') faz com que os valores baixos sejam verdes e os altos, vermelhos.
sns.heatmap(
    heatmap_data,
    annot=True,      # Escreve o valor da temperatura em cada célula
    fmt=".1f",       # Formata os números para ter uma casa decimal
    cmap='RdYlGn_r', # Define a paleta de cores: Verde (baixo) para Vermelho (alto)
    linewidths=.5    # Adiciona uma pequena linha entre as células
)

# Etapa 5: Adicionar títulos e rótulos
plt.title(f'Mapa de Calor da Temperatura Média (T2M) para {mes_para_visualizar}')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Etapa 6: Mostrar e/ou salvar o gráfico
plt.savefig('mapa_de_calor_temperatura.png') # Salva o gráfico como uma imagem
plt.show() # Mostra o gráfico em uma janela