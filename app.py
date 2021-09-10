


######################## Importar Librerias ##############################
import streamlit as st
import pandas as pd
import principal
import tablas
import graficos
from PIL import Image

################################################################
# Set the configs
APP_TITLE = "EXPLORACIÓN MODELO DE BLOQUES"
st.set_page_config(
    page_title = APP_TITLE,
    page_icon = Image.open('utils/pickaxe.png'),
    layout = "centered",
    initial_sidebar_state = "auto")
icon = Image.open('utils/pickaxe.png')


# External CSS
main_external_css = """
    <style>
        hr {margin: 15px 0px !important; background: #ff3a50}
        .footer {position: absolute; height: 50px; bottom: -150px; width:100%; padding:10px; text-align:center; }
        #MainMenu, .reportview-container .main footer {display: none;}
        .btn-outline-secondary {background: #FFF !important}
        .download_link {color: #f63366 !important; text-decoration: none !important; z-index: 99999 !important;
                        cursor:pointer !important; margin: 15px 0px; border: 1px solid #f63366;
                        text-align:center; padding: 8px !important; width: 200px;}
        .download_link:hover {background: #f63366 !important; color: #FFF !important;}
        h1, h2, h3, h4, h5, h6, a, a:visited {color: #054396 !important}
        label, stText, p, .caption {color: #000000 }
        .streamlit-expanderHeader {font-size: 16px !important;}
        .css-17eq0hr label, stText, .caption, .css-j075dz, .css-1t42vg8 {color: #000 !important}
        .css-17eq0hr a {text-decoration:underline;}
        .tickBarMin, .tickBarMax {color: #f84f57 !important}
        .markdown-text-container p {color: #035672 !important}
        .css-xq1lnh-EmotionIconBase {fill: #ff3a50 !important}
        .css-hi6a2p {max-width: 800px !important}
        /* Tabs */
        .tabs { position: relative; min-height: 200px; clear: both; margin: 40px auto 0px auto; background: #efefef; box-shadow: 0 48px 80px -32px rgba(0,0,0,0.3); }
        .tab {float: left;}
        .tab label { background: #f84f57; cursor: pointer; font-weight: bold; font-size: 18px; padding: 10px; color: #fff; transition: background 0.1s, color 0.1s; margin-left: -1px; position: relative; left: 1px; top: -29px; z-index: 2; }
        .tab label:hover {background: #035672;}
        .tab [type=radio] { display: none; }
        .content { position: absolute; top: -1px; left: 0; background: #fff; right: 0; bottom: 0; padding: 30px 20px; transition: opacity .1s linear; opacity: 0; }
        [type=radio]:checked ~ label { background: #035672; color: #fff;}
        [type=radio]:checked ~ label ~ .content { z-index: 1; opacity: 1; }
        /* Feature Importance Plotly Link Color */
        .js-plotly-plot .plotly svg a {color: #f84f57 !important}
    </style>
"""

st.markdown(main_external_css, unsafe_allow_html=True)
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
st.sidebar.markdown('# EXPLORACIÓN DE DATA CSV')
st.sidebar.markdown("<div style='text-align: justify'>Esta app está enfocada a un análisis exploratorio de datos de modelos de bloques y talaros de exploración visualizándola y calculando sus estadísticos básicos en Python.</div>", unsafe_allow_html=True)
st.sidebar.write("")
with st.sidebar.expander("GUÍA DE LA APLICACIÓN", expanded=False):
        st.info("""
        - Sube tu archivo excel / csv aquí. El tamaño máximo es 200 Mb.
        - Cada fila corresponde a una muestra, cada columna a una característica.
        - Escoge tu tipo de separador de tu csv.
        """)

separador=st.sidebar.selectbox(
'¿Cuál es el separador del CSV?',
(',',";",'/',' '))
uploadedfile = st.sidebar.file_uploader(' ', type=['.csv'])#PARA CARGAR MI ARCHIVO
st.sidebar.title('Menú de opciones')
options = st.sidebar.radio('Seleccione una página:', 
    ['TABLAS DE DATOS', 'GRÁFICOS','INFORMACIÓN'])
df = load_data(uploadedfile)#LO QUE CARGO LO METO A LA FUNCION
#################### Lista de Menus ###################
if options == 'TABLAS DE DATOS':
    tablas.tablas(df)
elif options == 'GRÁFICOS':
    graficos.graficos(df)
elif options == 'INFORMACIÓN':
    principal.principal()
