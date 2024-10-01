import pandas as pd

df = pd.read_csv('Track_file.csv')

# Exibir as primeiras linhas do DataFrame
print(df.head())
#Mostrar os valores máximo, mínimo e media da coluna 'Milliseconds'
print(df['Milliseconds'].min())
print(df['Milliseconds'].max())
print(df['Milliseconds'].mean())

df.groupby()
print('')