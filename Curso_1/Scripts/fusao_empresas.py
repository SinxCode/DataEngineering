import pandas as pd

#Leitura dos dados
dados_json = pd.read_json('C:/Users/gabrielbrito/Alura/PythonParaDataScience/Curso_1/Data_Raw/dados_empresaA.json')
dados_csv = pd.read_csv('C:/Users/gabrielbrito/Alura/PythonParaDataScience/Curso_1/Data_Raw/dados_empresaB.csv')

#Tratamento dos dados
dados_csv.columns=['Nome do Produto', 'Categoria do Produto', 'Preço do Produto (R$)', 'Quantidade em Estoque', 'Filial', 'Data da Venda']

#Unindo os dados
dados_combinados = pd.concat([dados_json, dados_csv], ignore_index=True)

#Salvando os dados
dados_combinados.to_csv('C:/Users/gabrielbrito/Alura/PythonParaDataScience/Curso_1/Data_Processed/dados_combinados.csv',index=False, encoding='utf-8')
