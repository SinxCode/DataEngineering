import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env


class DadosRepositorios:

#Iniciando a classe e definindo os parâmetros do Github
    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv("GITHUB_ACCESS_TOKEN")
        self.headers = {'Authorization': 'Bearer '+ self.access_token, 'X-GitHub-Api-Version': '2022-11-28'}

#Criando lista de repositórios
    def lista_repositorios(self):
        repos_list = []
        for page_num in range (1, 20):
            try:
             url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
             response = requests.get(url, headers=self.headers)
             repos_list.append(response.json())
            except:
                repos_list.append(None)
        
        return repos_list

#Pegando o nome dos repositórios dentro da lista anterior
    def nome_repos (self, repos_list):
        repos_names = []
        for page in repos_list:
            for repo in page:
                try:
                    repos_names.append(repo['name'])
                except:
                    pass
        
        return repos_names

 #Pegando a linguagem dos repositórios dentro da lista de repositórios   
    def nomes_linguagens(self, repos_list):
            repos_language = []
            for page in repos_list:
                for repo in page:
                    try:
                        repos_language.append(repo['language'])
                    except:
                        pass

            return repos_language

#Criando o DataFrame para armazenar os dados coletados em uma tabela
    def cria_df_linguagens(self):

        repositorios = self.lista_repositorios()
        nomes = self.nome_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens

        return dados

#obs: self é o objeto obrigatório que vem junto da clase que instancia os nosso métodos (funções) presente na nossa classe.



#Extraindo dados das empresas

#Amazon
amazon_rep = DadosRepositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()
#print(ling_mais_usadas_amzn)

#Netflix
netflix_rep = DadosRepositorios('netflix')
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

#Spotify
spotify_rep = DadosRepositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()


# Salvando os dados
ling_mais_usadas_amzn.to_csv('C:/Users/gabrielbrito/Alura/PythonParaDataScience/Curso_2/Data/linguagens_amzn.csv') 
ling_mais_usadas_netflix.to_csv('C:/Users/gabrielbrito/Alura/PythonParaDataScience/Curso_2/Data/linguagens_netflix.csv') 
ling_mais_usadas_spotify.to_csv('C:/Users/gabrielbrito/Alura/PythonParaDataScience/Curso_2/Data/linguagens_spotify.csv')        
        