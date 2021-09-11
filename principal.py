import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as components

def principal():
    #pweb = """<a href='http://www.idlmining.com/' target="_blank">http://www.idlmining.com/</a>"""
    st.title('Data Explorer IDL Mining - Version 0.1.3')
    col1, col2 = st.columns([2, 2])
    col1.markdown("<div style='text-align: justify'>Bienvenidos en esta app donde se podrá explorar los estadísticos básicos y visualizar modelos de bloques y taladros de exploración.</div>", unsafe_allow_html=True)
    col1.markdown("<div style='text-align: justify'>Si quieres conocer el codigo de esta app escrito en python puedes visitarlo en el siguiente enlace <a style='color:black; font-size:110% ;' href='https://github.com/CartagenaMinas/Data_Analisis_Mining' target='_blank'><i class='fa fa-rocket'></i>GitHub</a> </div>", unsafe_allow_html=True)
    col1.markdown("<div style='text-align: justify'>Tambien puedes visitar nuestra pagina web IDL Mining donde subimos post sobre programacion orientado a la ingeniera de minas y nos dedicamos a la creacion de Modelos de Deep Learning.</div>", unsafe_allow_html=True)
 
    chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=['a', 'b', 'c'])
    col2.area_chart(chart_data)
    st.write('### CREATED BY CRISTIAN CARTAGENA MATOS')
    components.html(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <a style="color:black; font-size:110% ;" href="https://www.linkedin.com/in/cristiancartagenamatos/" target="_blank"><i class="fa fa-linkedin-square"></i>Linkedin</a>
        <a style="color:black; font-size:110% ;" href="https://github.com/CartagenaMinas" target="_blank"><i class="fa fa-github"></i>Github</a>
        <a style="color:black; font-size:110% ;" href="http://www.idlmining.com/" target="_blank"><i class="fa fa-rocket"></i>IDL Mining</a>
        """  , height=600)

    
