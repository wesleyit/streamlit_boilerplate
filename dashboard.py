import sklearn.datasets
import streamlit as st
import pandas as pd
import plotly.express as px
import sklearn


# Configura o layout para usar o CSS customizado:
st.set_page_config(layout="wide")
with open( ".streamlit/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

@st.cache_data
def obtem_dados():
  '''Retorna uma lista contendo os datasets carregados.'''
  iris = sklearn.datasets.load_iris()
  df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
  return [df]

# Define 3 abas iniciais nas quais os dashboards serão exibidos:
tab1, tab2, tab3 = st.tabs([
    "Introdução", 
    "O Dataset", 
    "Conclusão"
])

with tab1:
  st.title("Introdução")
  st.markdown("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Nunc euismod, eros nec fringilla tristique, 
    justo purus fermentum purus, quis vehicula nulla nisl id est. 
    Donec nec purus id mi ultricies euismod. 
    Nunc auctor, dui ac suscipit semper, 
    justo erat tristique eros, quis lacinia erat lectus sit amet leo. 
    Pellentesque habitant morbi tristique sen.
  """)

with tab2:
  st.title("O Dataset")
  
  df = obtem_dados()[0]
  
  col1, col2 = st.columns([4,1])  
  col3, col4 = st.columns(2)

  col1.line_chart(df, use_container_width=True)
  col2.camera_input(label="Tire uma foto")
  col3.dataframe(df)
  col4.bar_chart(df, use_container_width=True)  

with tab3:
  st.title("Conclusão")
  st.markdown("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Nunc euismod, eros nec fringilla tristique, 
    justo purus fermentum purus, quis vehicula nulla nisl id est. 
    Donec nec purus id mi ultricies euismod. 
    Nunc auctor, dui ac suscipit semper, 
    justo erat tristique eros, quis lacinia erat lectus sit amet leo. 
    Pellentesque habitant morbi tristique sen.
  """)
