import requests
import base64

class Repositorio:
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = 'Insira um token'
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-Github-Api-Version': '2022-11-28'
        }
        
    def cria_repo(self, nome_repo):
        data = {
            "name": nome_repo,
            "description": "Dados dos repositório de algumas empresas",
            'private': False
        }
        response = requests.post(f"{self.api_base_url}/user/repos", 
                                 json=data, headers=self.headers)
        
        print(f'Status_code: {response.status_code}')
        
    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        with open(caminho_arquivo, 'rb') as file:
            file_content = file.read()
        enconded_content = base64.b64encode(file_content)
        
        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
        data = {
            'message': f'Adicionando arquivo {nome_arquivo}',
            'content': enconded_content.decode('utf-8')
        }
        
        response = requests.put(url, json=data, headers=self.headers)
        print(f'Status_code: {response.status_code}')
        
novo_repo = Repositorio('GustavoDallago')

nome_repo = 'linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo)

novo_repo.add_arquivo(nome_repo, '2. Dados/amazon.csv', '2. Dados/amazon.csv')
novo_repo.add_arquivo(nome_repo, '2. Dados/netflix.csv', '2. Dados/netflix.csv')
novo_repo.add_arquivo(nome_repo, '2. Dados/spotify.csv', '2. Dados/spotify.csv')