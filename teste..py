import numpy as pd
import streamlit as st
import oracledb
import pandas as pd

#st.title('Pagina de consulta de cadastro')
#st.write("Teste de pagina streamlit")
conn = oracledb.connect(user="rm551324", password="fiap23", dsn="oracle.fiap.com.br:1521/orcl") 
with conn.cursor() as c_consulta1:
    c_consulta1.execute("select * from t_pmm_comerciante")
    ldados = pd.DataFrame(c_consulta1.fetchall())
    ldados.columns = [x[0] for x in c_consulta1.description]
    print(ldados)
conn.close()