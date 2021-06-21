import streamlit as st
import numpy as np
import pandas as pd

def principal():
    #pweb = """<a href='http://www.idlmining.com/' target="_blank">http://www.idlmining.com/</a>"""
    st.title('Data Explorer IDL Mining - Version 0.1.3')
    st.write('## Bienvenidos al Explorador de Datos de CSV para modelos de Bloques y Taladros de Exploración')
    st.write('### Created by Cristian Cartagena Matos')
    #st.write(f'\nSi quieres saber mas sobre programación, el código o inteligencia artificial visita nuestra pagina web : {pweb}.', unsafe_allow_html=True)
    st.write('### Si quieres saber mas sobre programación, el código o inteligencia artificial visita nuestra pagina web ')
    chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=['a', 'b', 'c'])
    st.area_chart(chart_data)

    