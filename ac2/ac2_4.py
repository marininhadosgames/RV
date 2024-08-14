import streamlit as sl
sl.title("Calculadora de idades")
n=sl.text_input("Digite seu nome: ")
an=sl.number_input("Digite seu ano de nascimento: ")
aa=sl.number_input("Digite o ano atual: ")

ra=aa-an
rm=ra*12
rd=ra*365
if sl.button("Calcular em anos"):
    sl.text(ra)
if sl.button("Calcular em meses"):
    sl.text(rm)
if sl.button("Calcular em dias"):
    sl.text(rd)