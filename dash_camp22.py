import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide',page_title='Eleições 2022 (CE-MA-PI)')
st.title("Eleições 2022")
st.markdown("Visões sobre as Eleições brasileiras ano:2022")
candidatos_df = pd.read_csv('candidatos2022.csv',encoding='latin-1')

seleciona_estado = st.sidebar.selectbox('Qual estado você deseja vizualizar?',['TODOS','CE','MA','PI'])
if seleciona_estado == 'CE':
    candidatos_df = candidatos_df[candidatos_df['SG_UF']=='CE']
elif seleciona_estado == 'MA':
    candidatos_df = candidatos_df[candidatos_df['SG_UF']=='MA']
elif seleciona_estado == 'PI':
    candidatos_df = candidatos_df[candidatos_df['SG_UF']=='PI']
else:
    pass

sel_cargo = st.sidebar.selectbox('Qual o cargo pesquisado?',['GOVERNADOR','VICE-GOVERNADOR','DEPUTADO ESTADUAL','DEPUTADO FEDERAL','SENADOR','1º SUPLENTE','2º SUPLENTE'])
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

#Esse controle estava dando um erro porque não existe dados de candidados
#ao governo inapto e com isso um ValueError era lançado
#tentou-se resolver com try except sem sucesso
#logo deixaremos setado a variável para capturar somente os candidados aptos

seleciona_situacao = 'APTO'#st.sidebar.selectbox('Situação que você deseja vizualizar?',['Todos','APTO','INAPTO'])
if seleciona_situacao == 'APTO':
    candidatos_df = candidatos_df[candidatos_df['DS_SITUACAO_CANDIDATURA']=='APTO']
elif seleciona_situacao == 'INAPTO':
    candidatos_df = candidatos_df[candidatos_df['DS_SITUACAO_CANDIDATURA']=='INAPTO']
else:
    pass

seleciona_genero = st.sidebar.selectbox('Genero do Candidato?',['TODOS','MASCULINO','FEMININO'])
if seleciona_genero == 'MASCULINO':
    candidatos_df = candidatos_df[candidatos_df['DS_GENERO']=='MASCULINO']
elif seleciona_genero == 'FEMININO':
    candidatos_df = candidatos_df[candidatos_df['DS_GENERO']=='FEMININO']
else:
    pass

seleciona_raca = st.sidebar.selectbox('Raça que você deseja vizualizar?',['TODAS','BRANCA','PRETA','PARDA'])
if seleciona_raca == 'INDÍGENA':
    candidatos_df = candidatos_df[candidatos_df['DS_COR_RACA']=='INDÍGENA']
if seleciona_raca == 'AMARELA':
    candidatos_df = candidatos_df[candidatos_df['DS_COR_RACA']=='AMARELA']
if seleciona_raca == 'BRANCA':
    candidatos_df = candidatos_df[candidatos_df['DS_COR_RACA']=='BRANCA']
if seleciona_raca == 'PRETA':
    candidatos_df = candidatos_df[candidatos_df['DS_COR_RACA']=='PRETA']
if seleciona_raca == 'NÃO INFORMADA':
    candidatos_df = candidatos_df[candidatos_df['DS_COR_RACA']=='NÃO INFORMADA']
if seleciona_raca == 'PARDA':
    candidatos_df = candidatos_df[candidatos_df['DS_COR_RACA']=='PARDA']
else:
    pass

sel_estudo = 'TODOS'#st.sidebar.selectbox('Nível de instrução do candidato?',['TODOS','FUNDAMENTAL','MÉDIO','SUPERIOR'])
if sel_estudo == 'FUNDAMENTAL':
    candidatos_df = candidatos_df[candidatos_df['DS_CARGO']=='ENSINO FUNDAMENTAL']
elif sel_estudo == 'MÉDIO':
    candidatos_df = candidatos_df[candidatos_df['DS_CARGO']=='ENSINO MEDIO']
elif sel_estudo == 'SUPERIOR':
    candidatos_df = candidatos_df[candidatos_df['DS_CARGO']=='ENSINO SUPERIOR']
else:
    pass

col1,col2,col3,col4 = st.columns(4)
with col1:
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
    st.pyplot(fig)
with col2:
    ax = sns.color_palette("pastel")
    ax = sns.set_theme(style='darkgrid', palette='pastel')
    fig, ax = plt.subplots()
    fig = plt.figure(figsize=(5,5))
    ax = sns.countplot(x=candidatos_df['DS_CARGO'],hue=candidatos_df['DS_GENERO'])
    for p in ax.patches:
        ax.annotate('{}'.format(p.get_height()), (p.get_x()+0.12, p.get_height()+.05))
    plt.title('Gênero')
    plt.xlabel(" ")
    plt.ylabel(" ")
    st.pyplot(fig)
with col3:
    ax = sns.color_palette("pastel")
    ax = sns.set_theme(style='darkgrid', palette='pastel')
    fig, ax = plt.subplots()
    fig = plt.figure(figsize=(5,5))
    ax = sns.countplot(x=candidatos_df['DS_CARGO'],hue=candidatos_df['DS_COR_RACA'])
    for p in ax.patches:
        ax.annotate('{}'.format(p.get_height()), (p.get_x()+0.12, p.get_height()+.05))
    plt.title('Raça')
    plt.xlabel(" ")
    plt.ylabel(" ")
    st.pyplot(fig)
with col4:
    ax = sns.color_palette("pastel")
    ax = sns.set_theme(style='darkgrid', palette='pastel')
    fig, ax = plt.subplots()
    fig = plt.figure(figsize=(5,5))
    ax = sns.countplot(x=candidatos_df['DS_CARGO'],hue=candidatos_df['DS_GRAU_INSTRUCAO'])
    for p in ax.patches:
        ax.annotate('{}'.format(p.get_height()), (p.get_x()+0.12, p.get_height()+.05))
    plt.title('DS_Grau de Instrução')
    plt.xlabel(" ")
    plt.ylabel(" ")
    st.pyplot(fig)
