from googletrans import Translator
import streamlit as st

def traduzir_texto(texto, target_language='en'):
    try:
        tradutor = Translator()
        traducao = tradutor.translate(texto, dest=target_language)
        return traducao.text
    except Exception as e:
        return f"Erro na tradução: {e}"

# Exemplo de uso:
st.title('Tradutor Alemão')
st.subheader('Escreva coisas para serem traduzidas para alemão')

txt = st.text_input('Escreva aqui')

if txt:
    texto_traduzido = traduzir_texto(txt, target_language='de')
    st.write(texto_traduzido)
else:
    st.write("Digite um texto para traduzir.")
