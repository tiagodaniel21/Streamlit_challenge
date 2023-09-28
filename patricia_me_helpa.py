    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import re
    import string
    from wordcloud import WordCloud
    from datetime import datetime
    import locale

    area_plantio = pd.read_csv('areaPlatandaProducaoNacional.csv', encoding = 'latin1', sep=';')

    area_plantio['Ano Agricola.Ano Agricola'] = area_plantio['Ano Agricola.Ano Agricola'].str[:-3].astype(str)
    area_plantio['Area Plantada (mil ha)'] = area_plantio['Area Plantada (mil ha)'].str.replace(',', '').astype(float)
    area_plantio['Producao (mil t)'] = area_plantio['Producao (mil t)'].str.replace(',', '').astype(float)

    st.title('Dados sobre modalidade de linha de credito')

    st.write(area_plantio)

    st.write('Grafico com a Evolução da sua da area plantada')

    st.bar_chart(area_plantio, x=["Ano Agricola.Ano Agricola"], y=["Area Plantada (mil ha)"])