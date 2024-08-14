import streamlit as st
import random
usuario = 1234
senha= 9999
class item():
    def __init__(self, nome, preco):
        self.nome = nome
        self.codigo = 0
        self.preco = preco

items = [item('Cachorro quente', 8.50),
        item('Bauru simples', 4.50),
        item('Bauru com ovo', 5.50),
        item('Hamburguer',  5.50),
        item('Cheeseburguer', 6.60),
        item('Refrigerante', 6.00),
        item('Agua', 2.00),
        item('Suco de uva', 5.50),
        item('milky shakie', 6.75),
        ]
baseCode = 101
codigo = {}
for i in range(len(items)):
    if i >= baseCode:
        raise ValueError('limit of items reached!')
    codigo[baseCode + i] = items[i]
    items[i].codigo = baseCode + i

jps = 30
cardapioLayers = ['Lanche' + ' ' * (jps - 6) + 'Código' + ' ' * (jps - 6) + 'Valor' ]
for itemi in items:
    len1 = len(list(itemi.nome))
    len2 = len(list(str(itemi.codigo)))
    cardapioLayers.append(f'{itemi.nome}'  + ' ' * (jps - len1) + f'{itemi.codigo}' + ' ' * (jps - len2) + f'{itemi.preco}')

cardapio = 'cardápio: '
for i in cardapioLayers:
    cardapio += f'\n{i}'




st.title("Lanchonete")



#st.sidebar.subheader('mina')
#st.sidebar.checkbox('verd')
#st.sidebar.checkbox('falso')

userCode = st.text_input('Código de usuario: ')
password = st.text_input('Senha: ')
if userCode != '' and password != '':
    userCode = int(userCode)
    password = int(password)
    if userCode != usuario:
        st.text('O usuário está errado')
        can = False
    elif password != senha:
        st.text('A senha está errada')
        can = False
    else:
        can = True
else:
    can = False

suma = 0
if can == True:
    
    st.text('Acesso permitido')
    st.text(cardapio)
    st.text('Para pedir um produto escreva "codigo do produto : quantidade, codigo do produto : quantidade..."')
    productsStr = st.text_input('Produtos: ')
    if productsStr != '':
        products = productsStr.split(',')
        dor = []
        tds = []
        precu = 0
        for i in products:
           
            productSplit = i.split(':')
            code = productSplit[0]
            realCod = ''
            
            qtd = productSplit[1]
            realQtd = ''

            for i in list(code):
                if i != ' ':
                    realCod += i
            for i in list(qtd):
                if i != ' ':
                    realQtd += i
            
            evenMoreRealCod = int(realCod)
            evenMoreRealQtd = int(realQtd)

            dor.append(evenMoreRealCod)
            tds.append(evenMoreRealQtd)
        for i in range(len(tds)):
            precu += codigo[dor[i]].preco * tds[i]
        st.write(f'Preço Final: {precu}')
            
    
    
# python -m streamlit run your_script.py