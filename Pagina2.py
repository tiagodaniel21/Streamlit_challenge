import numpy as pd
import streamlit as st
import pandas as pd

from datetime import datetime
import locale

tabela_milho = pd.read_csv('export csv milho.csv', encoding = 'latin1', sep = ';', decimal = ',')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
tabela_milho['vigencia_final_ajustada'] = pd.to_datetime(tabela_milho['Vigência Final'], format = '%b-%Y')


st.title('Dados Sobre o Milho')

st.write('**Tabela com preços historicos do milho, desde 2014: **')

st.write(tabela_milho)

st.write('** Grafico do aumento do preço do milho: **')

st.bar_chart(
   tabela_milho, x="vigencia_final_ajustada", y=["Preço Mínimo"], color=["#38DD27"]  # Optional
)



