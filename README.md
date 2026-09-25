# Python - Consulta CEP API

Script em Python que consulta a API pública [ViaCEP](https://viacep.com.br/) e retorna o endereço (rua, bairro, cidade e estado) a partir de um CEP informado pelo usuário.

## 🎯 Objetivo

Projeto de estudo para praticar:
- Consumo de APIs REST com a biblioteca `requests`
- Tratamento de erros (CEP inválido, falha de conexão, timeout)
- Boas práticas de ambiente virtual (`venv`) e organização de projeto Python

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Yasminoliveirat/Python-Consulta-CEP-API.git
   cd Python-Consulta-CEP-API
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install requests
   ```

4. Rode o script:
   ```bash
   python3 teste.py
   ```

5. Digite um CEP quando solicitado (ex: `01001000`)

## 🛠️ Tecnologias utilizadas

- Python 3
- [requests](https://requests.readthedocs.io/) — para consumo da API
- [ViaCEP](https://viacep.com.br/) — API pública de consulta de CEP

## ⚙️ Funcionalidades

- Consulta de endereço a partir de um CEP digitado pelo usuário
- Tratamento de CEP inválido/inexistente
- Tratamento de erros de conexão e timeout
- Mensagens de erro específicas para cada tipo de falha

## 👩‍💻 Autora

Yasmin Oliveira Santos
