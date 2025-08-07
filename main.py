from tkinter import ttk
import tkinter as tk
from tkcalendar import DateEntry
import requests
from tkinter.filedialog import askopenfilename
import pandas as pd
import numpy as np
from datetime import datetime
import openpyxl
# palheta de cores
branco ='#FAFAFA'
preto ='#111111'
cinzaclaro ='#F2F2F2'
cinza ='#506773'
azul ='#6BAAD8'
vermelho ='#D35940'
laranja ='#F8D12B'
verde ='#05BC57'

lista_teste = [] # teste = list(dicionario_moedas.keys())
requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requisicao.json()
for bitcoin in dicionario_moedas:
    lista_teste.append(bitcoin)
def pegar_cotacao():
    moeda = combobox_selecionarmoedas.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes =data_cotacao[3:5]
    dia = data_cotacao[:2]
    link =  f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}"
    requisicao_moedas = requests.get(link)
    cotacao = requisicao_moedas.json()
    valor_moeda = cotacao[0]['bid']
    label_textocotacao['text'] = f"{moeda}  R$ {valor_moeda}"


def selecionar_arquivo():
    caminho = askopenfilename(title='Selecione o arquivo xlsx')
    var_caminhoarquivo.set(caminho)
    if caminho:
        label_arquivo = tk.Label(text=caminho, anchor='e', fg=laranja)
        label_arquivo.grid(row=6, padx=10, pady=10, sticky='nswe', columnspan=3)

def atualizar():
    try:
        # ler o dataframe de moedas
        df = pd.read_excel(var_caminhoarquivo.get())
        moedas = df.iloc[:, 0]
        # pegar a data de inicio e data de fim das cotacoes
        data_inicial = calendario_datainicial.get()
        data_final = calendario_datafinal.get()
        ano_inicial = data_inicial[-4:]
        mes_inicial = data_inicial[3:5]
        dia_inicial = data_inicial[:2]

        ano_final = data_final[-4:]
        mes_final = data_final[3:5]
        dia_final = data_final[:2]

        for moeda in moedas:
            link = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?" \
                   f"start_date={ano_inicial}{mes_inicial}{dia_inicial}&" \
                   f"end_date={ano_final}{mes_final}{dia_final}"

            requisicao_moeda = requests.get(link)
            cotacoes = requisicao_moeda.json()
            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%Y')
                if data not in df:
                    df[data] = np.nan

                df.loc[df.iloc[:, 0] == moeda, data] = bid
        df.to_excel("Teste.xlsx")
        label_atualizarcotacoes['text'] = "Arquivo Atualizado com Sucesso"
    except:
        label_atualizarcotacoes['text'] = "Arquivo Atualizado com Sucesso"

def fechar():
    janela.quit()


janela = tk.Tk()
janela.title('Sistema - Cotação')

label_cotacaomoeda = tk.Label(text='Cotação de 1 Moeda Especificada', borderwidth=2, relief='solid',fg=branco, bg=preto)
label_cotacaomoeda.grid(row=0, column=0, padx= 10, pady= 10, sticky='nswe', columnspan=3)

label_selecinarmoeda = tk.Label(text='Selecione a Moeda que deseja consultar', anchor='e', fg=cinza)
label_selecinarmoeda.grid(row=1, column=0, padx= 10, pady= 10, sticky='nswe', columnspan=2)
combobox_selecionarmoedas = ttk.Combobox(values=lista_teste)
combobox_selecionarmoedas.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecinardata = tk.Label(text='Selecione a Data', anchor='e', fg=cinza)
label_selecinardata.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
calendario_moeda = DateEntry(year=2025, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

label_textocotacao = tk.Label(text='', anchor='e')
label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
botao_pegar = tk.Button(text='Pegar Cotação',fg=branco, bg=azul, command=pegar_cotacao)
botao_pegar.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

# cotação de várias moedas
label_cotacaovariasmoeda = tk.Label(text='Cotação de Multiplas Moedas', borderwidth=2, relief='solid',fg=branco, bg=preto)
label_cotacaovariasmoeda.grid(row=4, column=0, padx= 10, pady= 10, sticky='nswe', columnspan=3)

label_selecinararquivo = tk.Label(text='Selecione o arquivo Excel da Moeda na Coluna A', fg=cinza)
label_selecinararquivo.grid(row=5, column=0, padx= 10, pady= 10, sticky='nswe', columnspan=2)
botao_selecionararquivo = tk.Button(text='Local',fg=branco, bg=azul, command=selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

var_caminhoarquivo = tk.StringVar()

label_arquivo = tk.Label(text='Nenhum Arquivo Selecionado ', anchor='e', fg=cinza)
label_arquivo.grid(row=6, padx=10, pady=10, sticky='nswe', columnspan=3)

label_datainicial = tk.Label(text='Data Inicial', fg=cinza)
label_datainicial.grid(row=7, column=1, padx=10, pady=10, sticky='nswe')

label_datafinal = tk.Label(text='Data Final',fg=cinza)
label_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='nswe')

calendario_datainicial = DateEntry(year=2025, locale='pt_br')
calendario_datainicial.grid(row=7, column=2, padx=10, pady=10, sticky='nswe')

calendario_datafinal = DateEntry(year=2025, locale='pt_br')
calendario_datafinal.grid(row=8, column=2, padx=10, pady=10, sticky='nswe')

label_atualizarcotacoes = tk.Label(text='')
label_atualizarcotacoes.grid(row=8, column=0, padx=10, pady=10, sticky='nswe')
botao_atualizar = tk.Button(text='Atualizar Cotação',fg=branco, bg=verde, command=atualizar)
botao_atualizar.grid(row=9, column=0, padx=10, pady=10, sticky='nswe')

botao_fecha = tk.Button(text='FECHA',fg=branco, bg=vermelho, command=fechar)
botao_fecha.grid(row=9, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()