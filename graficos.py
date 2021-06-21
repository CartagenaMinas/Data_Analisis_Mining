from os import write
import streamlit as st
import numpy as np
import pandas as pd
from traitlets.traitlets import default
from app import *
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

    
def graficos(df):
    st.title('Visualización de datos')
    options1=list(df.columns)
    categorical = st.selectbox(
    'Escoge tu variable categorica para desplegar en el grafico',
    options1)
    #categorical=list(categorical)
    cate=df[categorical].unique()
    
    if (len(cate)<50):
        df[categorical] = df[categorical].astype(str)
        fig = px.scatter_3d(df, x=options1[0], y=options1[1], z=options1[2], color=categorical)
        fig.update_traces(marker=dict(size=5.0))
        st.plotly_chart(fig, use_container_width=True)
    else:
        fig = px.scatter_3d(df, x=options1[0], y=options1[1], z=options1[2])
        fig.update_traces(marker=dict(size=5.0))
        st.plotly_chart(fig, use_container_width=True)

    options2=list(df.columns)
    continuous = st.selectbox(
    'Escoge tu variable continua para desplegar en el grafico',
    options2)
    cate2=df[continuous].unique()
    
    
    fig2 = px.scatter_3d(df, x=options1[0],  y=options1[1], z=options1[2], color=continuous, color_continuous_scale=px.colors.sequential.Jet, range_color=[0.0, df[continuous].quantile(0.95)])
    fig2.update_traces(marker=dict(size=5.0))
    st.plotly_chart(fig2, use_container_width=True)



    a=list(df.columns)
    options = st.multiselect(
    'De que quieres hacer un histograma',
    a,
    a[3])
    fig3 = px.histogram(
    data_frame=df,
    x=options,
    title="Histograma del Dataset",)
    fig3.update_traces(opacity=0.7)
    st.plotly_chart(fig3, use_container_width=True)



    b=list(df.columns)
    correla = st.multiselect(
    'De que quieres hacer un grafico de Correlacion',
    b,
    [b[0],b[1],b[2],b[3]])
    #st.write(correla)
    fig4 = sns.pairplot(df, vars=correla) 
    st.pyplot(fig4)

    





    

    