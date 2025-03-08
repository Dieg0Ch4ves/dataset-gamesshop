import pandas as pd
import os
# Obter o diretório atual
current_directory = os.path.dirname(os.path.abspath(__file__))
current_directory = os.path.dirname(current_directory)

# Construir o caminho completo para o arquivo Excel
file_path = os.path.join(current_directory, 'data', 'processed_data', 'Meganium_Sales_data.xlsx')

# Carregar o arquivo Excel
df = pd.read_excel(file_path)

# Filtrar as colunas necessárias
filtered_df = df[['delivery_country', 'quantity', 'product_sold']]

# Agrupar por país e produto, somando as quantidades
grouped_df = filtered_df.groupby(['delivery_country', 'product_sold']).sum().reset_index()

# Encontrar o produto mais vendido por país
most_sold_products = grouped_df.loc[grouped_df.groupby('delivery_country')['quantity'].idxmax()]

# Exibir o resultado
print(most_sold_products)