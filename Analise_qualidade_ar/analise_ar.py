import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#criando o caminho do arquivo para que o pandas o leia
caminho = "global_air_pollution_data.csv"
dados = pd.read_csv(caminho)

#consultando os primeiros valores
print(dados.head())

#resumo do dataset
print(dados.info())

#verificando a quantia de valores nulos para fazer a limpeza depois
print(dados.isnull().sum())


# # Verificar as linhas com valores nulos na coluna paises
# linhas_nulas_pais = dados[dados['Paises'].isnull()]
# print(linhas_nulas_pais)

# # Verificar as linhas com valores nulos na coluna paises
# linhas_nulas_cidades = dados[dados['Cidades'].isnull()]
# print(linhas_nulas_cidades)

#preencher as partes vazias para ficar nitido que esta faltando algum dados
dados['Paises'].fillna('Em Branco', inplace=True)
dados['Cidades'].fillna('Em Branco', inplace=True)







#verificar se foi retirado os com itens nulos
print(dados.isnull().sum())



#verificar os dados com que estamos trabalhando e suas categorias
print(dados['categoria_aqi'].unique())
print(dados['categoria_aqi_co'].unique())
print(dados['categoria_aqi_ozonio'].unique())
print(dados['categoria_aqi_no2'].unique())
print(dados['categoria_aqi_pm2.5'].unique())


# Resumo estatístico das colunas numéricas
print(dados.describe())



# Visualizar a distribuição dos valores de aqi
plt.figure(figsize=(10, 6))
sns.histplot(dados['valor_aqi'], kde=True, bins=30, color='blue')
plt.title('Distribuição dos Valores de aqi Global')
plt.xlabel('valor aqi')
plt.ylabel('Frequência')
plt.show()


# Contagem das categorias de aqi
plt.figure(figsize=(12, 6))
sns.countplot(data=dados, x='categoria_aqi', palette='Set2')
plt.title('Distribuição das Categorias de aqi')
plt.xlabel('Categoria de aqi')
plt.ylabel('Frequência')
plt.show()



# Relação entre aqi e co
plt.figure(figsize=(10, 6))
sns.scatterplot(data=dados, x='valor_aqi_co', y='valor_aqi', color='green')
plt.title('Relação entre aqi e co')
plt.xlabel('valor aqi co')
plt.ylabel('valor aqi')
plt.show()

# Relação entre aqi e ozonio
plt.figure(figsize=(10, 6))
sns.scatterplot(data=dados, x='valor_aqi_ozonio', y='valor_aqi', color='orange')
plt.title('Relação entre aqi e ozonio')
plt.xlabel('valor ozonio aqi')
plt.ylabel('valor aqi')
plt.show()

# Relação entre aqi e no2
plt.figure(figsize=(10, 6))
sns.scatterplot(data=dados, x='valor_aqi_no2', y='valor_aqi', color='red')
plt.title('Relação entre aqi e no2')
plt.xlabel('valor no2 aqi')
plt.ylabel('valora aqi')
plt.show()

# Relação entre aqi e pm2.5
plt.figure(figsize=(10, 6))
sns.scatterplot(data=dados, x='valor_aqi_pm2.5', y='valor_aqi', color='purple')
plt.title('Relação entre aqi e pm2.5')
plt.xlabel('valor pm2.5 aqi')
plt.ylabel('valor aqi')
plt.show()

# correlação entre as variáveis numéricas
correlation = dados[['valor_aqi', 'valor_aqi_co', 'valor_aqi_ozonio', 'valor_aqi_no2', 'valor_aqi_pm2.5']].corr()


# plot do  mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlação entre as variaveis de aqi')
plt.show()

# Calcular a media do aqi por país
aqi_por_pais = dados.groupby('Paises')['valor_aqi'].mean().sort_values(ascending=False)

# Paises com maiores numeros de aqi
plt.figure(figsize=(10, 8))
aqi_por_pais.head(20).plot(kind='bar', color='blue')
plt.title('Top 20 Países com os Maiores Valores medio de aqi (ar mais poluido)')
plt.xlabel('País')
plt.ylabel('aqi medio')
plt.xticks(rotation=90)
plt.show()


# Calcular a média do aqi por cidade
aqi_por_cidade = dados.groupby('Cidades')['valor_aqi'].mean().sort_values(ascending=True)

# cidades com os maiores numeros de aqi
plt.figure(figsize=(10, 8))
aqi_por_cidade.head(10).plot(kind='bar', color='green')
plt.title('Top 10 Cidades com os menores Valores medio de aqi (ar mais limpo)')
plt.xlabel('Cidade')
plt.ylabel('aqi medio')
plt.xticks(rotation=90)
plt.show()






