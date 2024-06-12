import streamlit as sl
import speech_recognition as sr

def principal():
    sl.title("Transcrição de audio: ")
    upload = sl.file_uploader("Faça upload do arquivo de áudio", type=["wav"])
    if upload is not None:
        transcrever(upload)

def transcrever(upload):
    recognizer = sr.Recognizer()
    with sr.AudioFile(upload) as source:
        sl.write("Processando...")
        audio = recognizer.record(source)
        texto = recognizer.recognize_google(audio,language="pt-BR")
        sl.write("Texto: ",texto)

principal()