# 💱 Sistema de Cotação de Moedas em Python
Este projeto é uma aplicação desktop criada em Python que permite consultar e atualizar cotações de moedas em tempo real, utilizando a API da AwesomeAPI.
O sistema foi desenvolvido com Tkinter para interface gráfica e Pandas para manipulação de dados financeiros.

🚀 Tecnologias utilizadas
Python 3

Tkinter + ttk + tkcalendar → Interface gráfica

Requests → Consumo da API de moedas

Pandas + Numpy + Openpyxl → Manipulação e exportação de dados para Excel

🎮 Funcionalidades
✔ Consulta da cotação de uma moeda específica em uma data escolhida
✔ Consulta e atualização de múltiplas moedas a partir de um arquivo Excel
✔ Exportação automática para novo arquivo Excel com as cotações atualizadas
✔ Interface gráfica simples e intuitiva

🏗 Estrutura do código
pegar_cotacao() → Busca a cotação de uma moeda específica em determinada data.

selecionar_arquivo() → Permite carregar um arquivo Excel com moedas na coluna A.

atualizar() → Percorre o Excel, consulta a API para o período escolhido e atualiza as cotações.

fechar() → Fecha a aplicação.

A interface conta com botões, calendários interativos e feedback visual das operações.

📊 Exemplo de uso
O usuário seleciona uma moeda (ex: USD) e uma data → o sistema exibe a cotação do dia.

O usuário seleciona um arquivo Excel com uma lista de moedas → define data inicial e final → cotações são buscadas e salvas em novo arquivo Excel.

💡 Aprendizados
Como integrar Python com APIs externas.

Construção de interfaces gráficas desktop com Tkinter.

Manipulação de arquivos Excel para relatórios financeiros.

Organização de fluxo de dados entre interface, API e persistência em arquivos.
