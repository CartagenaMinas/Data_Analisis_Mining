


######################## Importar Librerias ##############################
import streamlit as st
import pandas as pd
import principal
import tablas
import graficos





######################### Funciones #################################
def load_data(uploaded_file):#Funcion para cargar datos
    if uploaded_file is not None:#si uplode es diferente entonces
        try:#intento
            df = pd.read_csv(uploaded_file, sep=separador)
        except UnicodeDecodeError as e:#SALTA ERROR
            st.error(f"error loading log.las: {e}")
    else:
        df=None 
        df = pd.read_csv("db_mineralogia.csv", sep=",")
    return df



###################### SiderBar ########################################
st.sidebar.markdown('# Exploración de data CSV (Modelo de Bloques y Taladros de exploración)')
st.sidebar.write('Para usar esta app escoja un archivo en formato CSV para la exploración de datos.')
separador=st.sidebar.selectbox(
'¿Cuál es el separador del CSV?',
(',',";",'/',' '))
uploadedfile = st.sidebar.file_uploader(' ', type=['.csv'])#PARA CARGAR MI ARCHIVO
st.sidebar.title('Menú de opciones')
options = st.sidebar.radio('Seleccione una página:', 
    ['Menú principal', 'Tablas de datos','Graficos'])
df = load_data(uploadedfile)#LO QUE CARGO LO METO A LA FUNCION


#################### Lista de Menus ###################
if options == 'Menú principal':
    #pass
    principal.principal()
elif options == 'Tablas de datos':
    #pass
    tablas.tablas(df)
elif options == 'Graficos':
    graficos.graficos(df)
