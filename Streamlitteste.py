import numpy as pd
import streamlit as st
import pandas as pd

from datetime import datetime
import locale

tabela_milho = pd.read_csv('export csv milho.csv', encoding = 'latin1', sep = ';', decimal = ',')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
tabela_milho['vigencia_final_ajustada'] = pd.to_datetime(tabela_milho['Vigência Final'], format = '%b-%Y')
tabela_milho.groupby('vigencia_final_ajustada').sum()


print('Dados Sobre o Milho')

print('Tabela com preços historicos do milho, desde 2014: ')

print(tabela_milho)

print('Grafico do aumento do preço do milho: ')

#st.line_chart(
#   tabela_milho, x="vigencia_final_ajustada", y=["Preço Mínimo"]  # Optional
# )


# Agrupe os dados por estado e calcule a média do Preço Mínimo
media_por_estado = tabela_milho.groupby(['UF/Regiões amparadas', 'vigencia_final_ajustada'])['Preço Mínimo'].mean()

# Transforme o resultado em um novo DataFrame e redefina os índices
df_media_por_estado = media_por_estado.reset_index()

# Renomeie as colunas, se desejar
df_media_por_estado = df_media_por_estado.rename(columns={'UF/Regiões amparadas': 'Estado', 'Preço Mínimo': 'Média de Preço'})

# Exiba o DataFrame resultante
print(df_media_por_estado)