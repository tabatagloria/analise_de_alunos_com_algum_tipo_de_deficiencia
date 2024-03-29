# -*- coding: utf-8 -*-
"""analise de dados sobre o numero de estudantes deficientes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dy-3cC3hBGBsaBviXbcpxgJDRO8JP8no
"""

from google.colab import drive
import os

drive.mount('/content/gdrive')
os.chdir("/content/gdrive/My Drive/Colab Notebooks")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

low_memory=False
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90

data = pd.read_csv(r'DM_ALUNO.CSV', delimiter='|', encoding='iso-8859-1', usecols=['ID_ALUNO','TP_SEXO','IN_DEFICIENCIA','NU_IDADE','NU_ANO_INGRESSO'])

'''
  Análise do total de pessoas que possuam alguma deficiência
'''

data.shape

data.rename(columns={'ID_ALUNO':'Id','TP_SEXO':'Sexo','NU_IDADE':'Idade','IN_DEFICIENCIA':'Possui_Deficiencia'},inplace=True)
data.sample(10)

data.groupby('Sexo').size().sort_values().plot(kind='barh')

total = data.query('Possui_Deficiencia == 1')['Id'].count()
f'Quantidade de pessoas com algum tipo de dificiência: {total}'

mulheres = data.query('Possui_Deficiencia == 1 and Sexo == 1')['Id'].count()
f'Quantidade de mulheres com algum tipo de dificiência: {mulheres}'

f'Porcentagem de mulheres: {mulheres / total * 100:.2f}%'

homens = data.query('Possui_Deficiencia == 1 and Sexo == 2')['Id'].count()
f'Quantidade de homens com algum tipo de dificiência: {homens}'

f'Porcentagem de homens: {homens / total * 100:.2f}%'

''' Faixa etária de 18 anos ''' 

mulheres = data.query('Possui_Deficiencia == 1 and Sexo == 1 and Idade == 18')['Id'].count()
f'Quantidade de mulheres: {mulheres}'

homens = data.query('Possui_Deficiencia == 1 and Sexo == 2 and Idade == 18')['Id'].count()
f'Quantidade de mulheres: {homens}'

total = data.query('Possui_Deficiencia == 1 and Idade == 18')['Id'].count()
f'Quantidade de mulheres: {total}'

'''
  Análise anual: 2016, 2017, 2018
'''

ano_2016 = data.query('NU_ANO_INGRESSO == 2016')['Id'].count()
f'Quantidade: {ano_2016}'

total = data.query('Possui_Deficiencia == 1 and NU_ANO_INGRESSO == 2016')['Id'].count()
f'Quantidade de pessoas com algum tipo de dificiência: {total}'

mulheres = data.query('Possui_Deficiencia == 1 and Sexo == 1 and NU_ANO_INGRESSO == 2016')['Id'].count()
f'Quantidade de mulheres com algum tipo de dificiência no ano de 2016: {mulheres}'

homens = data.query('Possui_Deficiencia == 1 and Sexo == 2 and NU_ANO_INGRESSO == 2016')['Id'].count()
f'Quantidade de mulheres com algum tipo de dificiência no ano de 2016: {homens}'

f'Porcentagem de mulheres: {mulheres / total * 100:.2f}%, Porcentagem de homens: {homens / total * 100:.2f}%'

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

f2016 = [mulheres]
m2016 = [homens]

barWidth = 0.25

plt.figure(figsize=(10,5))

r1 = np.arange(len(f2016))
r2 = [x + barWidth for x in r1]

plt.bar(r1, f2016, color="#ff94ab", width=barWidth, label="Feminino")
plt.bar(r2, m2016, color="#38b0de", width=barWidth, label="Masculino")

plt.xlabel('Sexo')
plt.ylabel('Quantidade')
plt.xticks([r + barWidth for r in range(len(f2016))], ['2016'])

plt.legend()
plt.savefig('histograma-2016.png')
plt.show()
plt.close()



ano_2017 = data.query('NU_ANO_INGRESSO == 2017')['Id'].count()
f'Quantidade: {ano_2017}'

total = data.query('Possui_Deficiencia == 1 and NU_ANO_INGRESSO == 2017')['Id'].count()
f'Quantidade de pessoas com algum tipo de dificiência: {total}'

mulheres = data.query('Possui_Deficiencia == 1 and Sexo == 1 and NU_ANO_INGRESSO == 2017')['Id'].count()
f'Quantidade de mulheres com algum tipo de dificiência no ano de 2016: {mulheres}'

homens = data.query('Possui_Deficiencia == 1 and Sexo == 2 and NU_ANO_INGRESSO == 2017')['Id'].count()
f'Quantidade de mulheres com algum tipo de dificiência no ano de 2016: {homens}'

f'Porcentagem de mulheres: {mulheres / total * 100:.2f}%, Porcentagem de homens: {homens / total * 100:.2f}%'

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

f2017 = [mulheres]
m2017 = [homens]

barWidth = 0.25

plt.figure(figsize=(10,5))

r1 = np.arange(len(f2017))
r2 = [x + barWidth for x in r1]

plt.bar(r1, f2017, color="#ff94ab", width=barWidth, label="Feminino")
plt.bar(r2, m2017, color="#38b0de", width=barWidth, label="Masculino")

plt.xlabel('Sexo')
plt.ylabel('Quantidade')
plt.xticks([r + barWidth for r in range(len(f2016))], ['2017'])

plt.legend()
plt.savefig('histograma-2017.png')
plt.show()
plt.close()



ano_2018 = data.query('NU_ANO_INGRESSO == 2018')['Id'].count()
f'Quantidade: {ano_2018}'

total = data.query('Possui_Deficiencia == 1 and NU_ANO_INGRESSO == 2018')['Id'].count()
f'Quantidade de pessoas com algum tipo de dificiência: {total}'

mulheres = data.query('Possui_Deficiencia == 1 and Sexo == 1 and NU_ANO_INGRESSO == 2018')['Id'].count()
f'Quantidade de mulheres com algum tipo de dificiência no ano de 2016: {mulheres}'

homens = data.query('Possui_Deficiencia == 1 and Sexo == 2 and NU_ANO_INGRESSO == 2018')['Id'].count()
f'Quantidade de mulheres com algum tipo de dificiência no ano de 2016: {homens}'

f'Porcentagem de mulheres: {mulheres / total * 100:.2f}%, Porcentagem de homens: {homens / total * 100:.2f}%'

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

f2018 = [mulheres]
m2018 = [homens]

barWidth = 0.25

plt.figure(figsize=(10,5))

r1 = np.arange(len(f2018))
r2 = [x + barWidth for x in r1]

plt.bar(r1, f2018, color="#ff94ab", width=barWidth, label="Feminino")
plt.bar(r2, m2018, color="#38b0de", width=barWidth, label="Masculino")

plt.xlabel('Sexo')
plt.ylabel('Quantidade')
plt.xticks([r + barWidth for r in range(len(f2018))], ['2018'])

plt.legend()
plt.savefig('histograma-2018.png')
plt.show()
plt.close()

