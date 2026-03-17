import requests
import pandas as pd
from math import ceil

class DadosRepositorios:
    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = 'Insira um token'
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-Github-Api-Version': '2022-11-28'
        }
        
    def lista_repositorios(self):
        repos_list = []
        
        response = requests.get(f'https://api.github.com/users/{self.owner}')
        num_pages = ceil(response.json()['public_repos']/30)

        for page_num in range (1, num_pages+1):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        return repos_list
    
    def nomes_repos(self, repos_list):
        repos_name = []

        for page in repos_list:
            for repo in page:
                try:
                    repos_name.append(repo['name'])
                except:
                    pass
        return repos_name
    
    def linguagens_repos(self, repos_list):
        repos_linguagens = []

        for page in repos_list:
            for repo in page:
                try:
                    repos_linguagens.append(repo['language'])
                except:
                    pass
        return repos_linguagens
    
    def cria_df_linguagens(self):
        

        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.linguagens_repos(repositorios)
        
        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens
        
        return dados
    
amazon_rep = DadosRepositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()

netflix_rep = DadosRepositorios('netflix')
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

spotify_rep = DadosRepositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()

# Salvando os dados em arquivos CSV

ling_mais_usadas_amzn.to_csv('2. Dados/amazon.csv', index=False)
ling_mais_usadas_netflix.to_csv('2. Dados/netflix.csv', index=False)
ling_mais_usadas_spotify.to_csv('2. Dados/spotify.csv', index=False)