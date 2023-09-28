import streamlit as st
import matplotlib.pyplot as plt

##Pagina 0 
def home_page():
    import streamlit as st
    import matplotlib.pyplot as plt
    from PIL import Image

    logo = Image.open('logo.png')
    st.title("Bem vindo Usuário, ao Sistema da")
    st.image(logo)
    st.subheader('Para informações: ')
    st.write("Aqui, você terá acesso rápido e fácil a informações valiosas relacionadas ao crédito rural. Se você é um agricultor, um investidor ou alguém interessado no setor agrícola, nossa plataforma é a sua porta de entrada para dados confiáveis e atualizados. \
\
O crédito rural desempenha um papel fundamental no desenvolvimento e na sustentabilidade da agricultura. Com nossa aplicação, você pode:\
\
Acessar Informações Cruciais: Consulte dados sobre empréstimos, taxas de juros, prazos e muito mais para tomar decisões informadas.\
\
Analisar Tendências: Acompanhe as tendências do mercado agrícola e do crédito rural para tomar decisões estratégicas.\
\
Ferramentas de Tomada de Decisão: Utilize nossas ferramentas de análise e projeção para planejar seus investimentos com confiança.\
\
Conexão com Especialistas: Entre em contato com especialistas em crédito rural para obter orientações personalizadas.\
\
Nossa aplicação foi projetada para ser intuitiva e fácil de usar, para que você possa encontrar as informações de que precisa sem complicações. No setor agrícola, o conhecimento é poder, e nossa plataforma está aqui para capacitar sua jornada no crédito rural.\
\
Comece agora mesmo a explorar nossos recursos e a tomar decisões financeiras mais inteligentes no mundo do crédito rural. Estamos aqui para apoiá-lo em cada passo do caminho.\
\
Agrícola com confiança. Consulte com sabedoria.")







## Pagina 1
def consulta_comerciante():
    import numpy as pd
    import streamlit as st
    import oracledb
    import pandas as pd

    st.title('Pagina de consulta de cadastro')
    st.write("Teste de pagina streamlit")

    conn = oracledb.connect(user="rm551324", password="fiap23", dsn="oracle.fiap.com.br:1521/orcl")

    with conn.cursor() as c_consulta1:
        c_consulta1.execute("select * from t_pmm_comerciante")
        ldados = pd.DataFrame(c_consulta1.fetchall())
        ldados.columns = [x[0] for x in c_consulta1.description]
        teste = ldados['DS_NIVEL_COMERCIALIZACAO']
        direito_cred = []
        for i in teste:
            if i == 1:
                direito_cred.append("R$ 10000")
            elif i == 2:
                direito_cred.append("R$ 20000")
            elif i == 3:
                direito_cred.append("R$ 30000")
            else:
                direito_cred.append("R$ 60000")

        ldados['Direito de Credito'] = direito_cred
        st.write(ldados)











## Pagina 2
def pagina_milho():
    import numpy as pd
    import streamlit as st
    import pandas as pd

    from datetime import datetime
    import locale

    tabela_milho = pd.read_csv('export csv milho.csv', encoding = 'latin1', sep = ';', decimal = ',')
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    tabela_milho['vigencia_final_ajustada'] = pd.to_datetime(tabela_milho['Vigência Final'], format = '%b-%Y')
    media_por_estado = tabela_milho.groupby(['UF/Regiões amparadas', 'vigencia_final_ajustada'])['Preço Mínimo'].mean()
    df_media_por_estado = media_por_estado.reset_index()
    df_media_por_estado = df_media_por_estado.rename(columns={'UF/Regiões amparadas': 'Estado', 'Preço Mínimo': 'media_preco'})


    st.title('Dados Sobre o Milho')

    st.subheader('Tabela com preços historicos do milho, desde 2014: ')

    st.write(tabela_milho)

    st.subheader('Grafico do aumento do preço do milho: ')

    st.line_chart(
       df_media_por_estado, x="vigencia_final_ajustada", y="media_preco"  # Optional
    )









## Pagina 3
def pagina_modalidade():
    import numpy as pd
    import streamlit as st
    import pandas as pd

    from datetime import datetime
    import locale

    modalidade = pd.read_csv('ProgramaModalidade.csv', encoding = 'latin1')


    st.title('Dados sobre modalidade de linha de credito')

    st.write(modalidade)






## Pagina 4
def pagina_area_plantio():
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import re
    import string
    from wordcloud import WordCloud
    from datetime import datetime
    import locale

    area_plantio = pd.read_csv('areaPlatandaProducaoNacional.csv', encoding = 'latin1', sep=';')

    area_plantio['Ano Agricola'] = area_plantio['Ano Agricola.Ano Agricola'].str[:-3].astype(str)
    area_plantio['Area Plantada (mil ha)'] = area_plantio['Area Plantada (mil ha)'].str.replace(',', '').astype(float)
    area_plantio['Producao (mil t)'] = area_plantio['Producao (mil t)'].str.replace(',', '').astype(float)

    st.title('Dados sobre modalidade de linha de credito')

    st.write(area_plantio)

    st.write('Grafico com a Evolução da sua da area plantada')

    st.bar_chart(area_plantio, x="Ano Agricola", y=["Area Plantada (mil ha)", "Producao (mil t)"])






#Pagina 5
def pagina_Quantidade_valor():
    import numpy as pd
    import streamlit as st
    import pandas as pd

    from datetime import datetime
    import locale

    Quantidade_valor = pd.read_csv('RelatorioQuantidade e Valor dos Contratos por Região e UF 19-05-2023.csv', encoding = 'utf-8')
    quantidade_valor_limpa = Quantidade_valor.drop(columns = ['Textbox28', 'Textbox37','Textbox38', 'Textbox39', 'Textbox40',
                                                          'Textbox41', 'Textbox46', 'Textbox31', 'Textbox32',
                                                          'Textbox53', 'Textbox33', 'Textbox34', 'Textbox35', 'Textbox36',
                                                          'Textbox17', 'Textbox48', 'Textbox59', 'Textbox4', 'Textbox11',
                                                          'Textbox47', 'Textbox22', 'Textbox23', 'Textbox54', 'Textbox24',
                                                          'Textbox25', 'Textbox26', 'Textbox27', 'Textbox42', 'Textbox49',
                                                          'Textbox60', 'Textbox5', 'Textbox12'])

    st.title('Dados sobre Quantidade e valor')
    st.write(quantidade_valor_limpa)








##Menu sideBar
page_names_to_funcs = {
    "Pagina inicial": home_page,
    "Cotação Histórica Milho": pagina_milho,
    "Consulta de cadastro de comerciantes": consulta_comerciante,
    "Consulta das modalidades de credito": pagina_modalidade,
    "Dados da Area de plantio e dados de produção historicos": pagina_area_plantio,
    "dados por região de Quantidade e valor": pagina_Quantidade_valor
}
demo_name = st.sidebar.selectbox("Escolha Qual pesquisa deseja realizar", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
