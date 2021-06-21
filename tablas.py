import streamlit as st
import numpy as np
import pandas as pd
from traitlets.traitlets import default
from app import *
import plotly.express as px
import matplotlib.pyplot as plt

    
def tablas(df):
    st.title('Tabla de Datos')
    st.write(df)
    dfd=df.describe().T
    st.title('Estadísticos generales')
    st.write(dfd)
    st.title('Ver valores únicos según columna')
    valores_unicos=list(df.columns)
    options = st.selectbox(
    '¿Que columna quieres ver los valores únicos?',
    valores_unicos)
    df_unicos=df[options].unique()
    st.write(df_unicos)
