import streamlit as st
import numpy as np
import pandas as pd
from traitlets.traitlets import default
import plotly.express as px
import matplotlib.pyplot as plt

    
def tablas(df):
    st.title('TABLA DE DATOS')
    st.write(df)
    dfd=df.describe().T
    st.title('ESTADÍSTICOS GENERALES')
    st.write(dfd)
    st.title('VER VALORES ÚNICOS SEGÚN COLUMNA')
    valores_unicos=list(df.columns)
    options = st.selectbox(
    '¿Que columna quieres ver los valores únicos?',
    valores_unicos)
    df_unicos=df[options].unique()
    st.write(df_unicos)
