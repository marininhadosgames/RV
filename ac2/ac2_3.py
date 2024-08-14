import streamlit as sl
sl.title("Veja seu desconto!")
n=sl.text_input("Digite seu nome: ")
p=sl.number_input("Digite o preço: ",min_value=0.0,format="%.2f")
sl.text("Códigos de Origem\nRegião Norte - 1\nRegião Sul - 2\nRegião Sudeste - 3\nRegião Nordeste - 4\nRegião Centro-Oeste - 5")
co=sl.number_input("Digite o código de origem: ",min_value=0.0,format="%.2f")

if co==1:
    sl.text("Seu desconto é de 5%")
    sl.write(f"Seu valor com desconto é {p*0.95}")
if co==2:
    sl.text("Seu desconto é de 15%")
    sl.write(f"Seu valor com desconto é {p*0.75}")
if co==3:
    sl.text("Seu desconto é de 7%")
    sl.write(f"Seu valor com desconto é {p*0.93}")
if co==4:
    sl.text("Seu desconto é de 12%")
    sl.write(f"Seu valor com desconto é {p*0.88}")
if co==5:
    sl.text("Seu desconto é de 20%")
    sl.write(f"Seu valor com desconto é {p*0.80}")
