import requests


try:
    CEP = input("Digite o CEP: ")
    response = requests.get(f"https://viacep.com.br/ws/{CEP}/json/", timeout=5)
    DADOS = response.json()
    print(response.json())

    if 'erro' in DADOS:
        print("CEP inválido.")
    else:
        print(f"CEP: {DADOS['cep']}")
        print(f"Logradouro: {DADOS['logradouro']}")
        print(f"Bairro: {DADOS['bairro']}")
        print(f"Cidade: {DADOS['localidade']}")
        print(f"Estado: {DADOS['uf']}")

except requests.exceptions.RequestException as e:   
    print(f"Erro na requisição: {e}")