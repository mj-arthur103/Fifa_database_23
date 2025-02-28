import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime
st.set_page_config(
    layout='wide',
    page_title='Fifa 23 Info',
)

if 'data' not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until']>= datetime.today().year]
    df_data = df_data[df_data['Value(£)']>0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data']=df_data

st.markdown('# Fifa 23 Info!')
st.sidebar.markdown('Dev Arthur Carneiro')

btn=st.button('Acesse os dados do Kaggle')
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset')

st.markdown(
    """"
    O conjunto de dados de jogadores de futebol de 2023, vai ser apresentado agora.
    """
)
