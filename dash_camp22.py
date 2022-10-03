import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide',page_title='Eleições 2022 (CE-MA-PI)')
st.title("Eleições 2022")
st.markdown("Visões sobre as Eleições brasileiras ano:2022")
candidatos_df = pd.read_csv('candidatos2022.csv',encoding='latin-1')

seleciona_estado = st.sidebar.selectbox('Qual estado você deseja vizualizar?',['Todos','CE','MA','PI'])
if seleciona_estado == 'CE':
    candidatos_df = candidatos_df[candidatos_df['SG_UF']=='CE']
elif seleciona_estado == 'MA':
    candidatos_df = candidatos_df[candidatos_df['SG_UF']=='MA']
elif seleciona_estado == 'PI':
    candidatos_df = candidatos_df[candidatos_df['SG_UF']=='PI']
else:
    pass

sel_cargo = st.sidebar.selectbox('Qual o campo pesquisado?',['GOVERNADOR','VICE-GOVERNADOR','DEPUTADO ESTADUAL','DEPUTADO FEDERAL','SENADOR','1º SUPLENTE','2º SUPLENTE'])
if sel_cargo == 'GOVERNADOR':
    candidatos_df = candidatos_df[candidatos_df['DS_CARGO']=='GOVERNADOR']
elif sel_cargo == 'VICE-GOVERNADOR':
    candidatos_df = candidatos_df[candidatos_df['DS_CARGO']=='VICE-GOVERNADOR']
elif sel_cargo == 'DEPUTADO ESTADUAL':
    candidatos_df = candidatos_df[candidatos_df['DS_CARGO']=='DEPUTADO ESTADUAL']
elif  sel_cargo == 'DEPUTADO FEDERAL':
    candidatos_df = candidatos_df[candidatos_df['DS_CARGO']=='DEPUTADO FEDERAL']
elif  sel_cargo == 'SENADOR':
    candidatos_df = candidatos_df[candidatos_df['DS_CARGO']=='SENADOR']
elif   sel_cargo == '1º SUPLENTE':
    candidatos_df = candidatos_df[candidatos_df['DS_CARGO']=='1º SUPLENTE']
else:
    candidatos_df = candidatos_df[candidatos_df['DS_CARGO']=='2º SUPLENTE']

ax = sns.color_palette("pastel")
ax = sns.set_theme(style='darkgrid', palette='pastel')
fig, ax = plt.subplots()
fig = plt.figure(figsize=(5,5))
ax = sns.countplot(x=candidatos_df['DS_CARGO'],hue=candidatos_df['SG_UF'])
for p in ax.patches:
    ax.annotate('{}'.format(p.get_height()), (p.get_x()+0.12, p.get_height()+.05))
plt.title('Cargo')
plt.xlabel(" ")
plt.ylabel(" ")

col1,col2,col3 = st.columns(3)
with col1:
    st.pyplot(fig)
with col2:
    st.title("XXXXXXXXXXXXXx")
with col3:
    st.title("XXXXXXXXXXXXXXx")
