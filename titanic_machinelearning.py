# -*- coding: utf-8 -*-
"""Titanic_MachineLearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bMcFEGZ9Xz0BGj-5YOdkT6hcda3AaMdQ
"""

# BIBLIOTECAS
import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# IMPORTANDO DIRETO DO GITHUB DATASET
titanicTrain = pd.read_csv('https://raw.githubusercontent.com/guftrindade/Titanic_MachineLearning/main/train.csv')
titanicTrain.head()

"""#**Pré-Processamento**

##Conhecendo os dados de treino
"""

# ANÁLISE DESCRITIVA DOS DADOS
titanicTrain.describe()

# IDADES COM VALOR NULO RECEBENDO O NÚMERO -1
titanicTrain['Age'][titanicTrain['Age'].isnull()] = -1

titanicTrain['Age'][titanicTrain['Age'] <0]

# MÉDIA DE IDADE DA COLUNA 'AGE' SEM OS DADOS FALTANTES
media = round((titanicTrain['Age'][titanicTrain['Age']>0].mean()),2)
media

# INSERINDO A MÉDIA DE IDADE NAS COLUNAS COM IDADE 0
titanicTrain.loc[titanicTrain['Age'] < 0,'Age'] = media

# VERIFICANDO COLUNA IDADE NOVAMENTE
titanicTrain['Age'].isnull().sum()

# VERIFICANDO O TIPO DE CADA COLUNA DE DADOS
titanicTrain.info()

# VERIFICANDO QUANTIDADE DE SOBREVIVENTES E NÃO SOBREVIVENTES
titanicTrain.Survived.value_counts()

# VISUALIZANDO NOVAMENTE TODO O DATASET
titanicTrain

"""##Visualizando os dados"""

plt.figure(figsize=(6,4))
sns.countplot(x = titanicTrain['Survived']);
plt.title('PLOTAGEM DO NÚMERO DE SOBREVIVENTES')
plt.show()

# IDADE E SEXO DOS PASSAGEIROS
sns.boxplot(x='Sex', y='Age', data=titanicTrain)
plt.title('DISTRIBUIÇÃO DE SEXO E IDADE DOS PASSAGEIROS')
plt.figure(figsize=(6,4))
plt.show()

# GRÁFICO DE HISTOGRAMA DA COLUNA IDADE
plt.figure(figsize=(6,4))
plt.hist(x=titanicTrain['Age'])
plt.title('HISTOGRAMA DA IDADE DOS PASSAGEIROS')
plt.show()

# GRÁFICO DE HISTOGRAMA DA COLUNA CLASSE
plt.figure(figsize=(6,4))
sns.countplot(x=titanicTrain['Pclass'])
plt.title('QUANTIDADE DE PASSAGEIROS POR CLASSE')
plt.show()

# GRÁFICO DINAMICO IDADE X SOBREVIVENTES
grafico = px.scatter_matrix(titanicTrain, dimensions=['Age'], color = 'Survived')
grafico.show()

# GRÁFICO DINAMICO CLASSE X IDADE X SOBREVIVENTES
grafico = px.scatter_matrix(titanicTrain, dimensions=['Pclass','Age'], color = 'Survived')
grafico.show()

# GRÁFICO DINAMICO CLASSE X IDADE X SEXO X SOBREVIVENTES
grafico = px.scatter_matrix(titanicTrain, dimensions=['Pclass','Age','Sex'], color = 'Survived')
grafico.show()

# GRÁFICO DE CATEGORIA PARALELA
grafico = px.parallel_categories(titanicTrain, dimensions=['Sex','Pclass','Survived'])
grafico.show()

titanicTrain

"""#**Modelagem Treino**

##Variáveis X e Y - Treino
"""

# DROP COLUNA NAMES
titanicTrain.drop(columns=['Name'])

# Alocando todas as linhas das colunas Classe, Sexo e Idade
xtitanicTrain = titanicTrain.drop(columns=['Name']).iloc[:,2:5].values
xtitanicTrain

# Alocando a coluna 'Survived' em Y
ytitanicTrain = titanicTrain.iloc[:,1]
ytitanicTrain

# TRANSFORMADO A COLUNA SEXO EM (1,0)
xtitanicTrain[:,1]

from sklearn.preprocessing import LabelEncoder

xtitanicTrain[:,1] = LabelEncoder().fit_transform(xtitanicTrain[:,1])

xtitanicTrain

xtitanicTrain.shape, ytitanicTrain.shape

"""#Modelagem Teste"""

titanicTest = pd.read_csv('https://raw.githubusercontent.com/guftrindade/Titanic_MachineLearning/main/test.csv')
titanicTest

titanicTest.info()

"""##Conhecendo os dados de teste"""

# ANÁLISE DESCRITIVA DOS DADOS
titanicTest.describe()

# IDADES COM VALOR NULO RECEBENDO O NÚMERO -1
titanicTest['Age'][titanicTest['Age'].isnull()] = -1

titanicTest['Age'][titanicTest['Age'] <0]

# MÉDIA DE IDADE DA COLUNA 'AGE' SEM OS DADOS FALTANTES
media = round((titanicTest['Age'][titanicTest['Age']>0].mean()),2)
media

# INSERINDO A MÉDIA DE IDADE NAS COLUNAS COM IDADE 0
titanicTest.loc[titanicTest['Age'] < 0,'Age'] = media

# VERIFICANDO COLUNA IDADE NOVAMENTE
titanicTest['Age'].isnull().sum()

# VERIFICANDO O TIPO DE CADA COLUNA DE DADOS
titanicTest.info()

# VISUALIZANDO NOVAMENTE TODO O DATASET
titanicTest

"""##Variáveis X e Y - Teste"""

# Alocando todas as linhas das colunas Classe, Sexo e Idade
xtitanicTest = titanicTest.drop(columns=['Name']).iloc[:,1:4].values
xtitanicTest

# TRANSFORMADO A COLUNA SEXO EM (1,0)
xtitanicTest[:,1]

from sklearn.preprocessing import LabelEncoder

xtitanicTest[:,1] = LabelEncoder().fit_transform(xtitanicTest[:,1])
xtitanicTest

# ALOCANDO AS VARIÁVEIS EM Y_TESTE
titanicTestSubmission = pd.read_csv('https://raw.githubusercontent.com/guftrindade/Titanic_MachineLearning/main/gender_submission.csv')
titanicTestSubmission

ytitanicTest = titanicTestSubmission.iloc[:,1]
ytitanicTest

"""#**Machine Learning**"""

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from yellowbrick.classifier import ConfusionMatrix

"""##**Regressão Logística - 95,93%**"""

# REALIZANDO O TREINAMENTO DO MODELO
from sklearn.linear_model import LogisticRegression
logisticTitanic = LogisticRegression(random_state=1)
logisticTitanic.fit(xtitanicTrain,ytitanicTrain)

# VERIFICANDO A INTERCEPTAÇÃO
logisticTitanic.intercept_

# COEFICIENTE
logisticTitanic.coef_

previsoes = logisticTitanic.predict(xtitanicTest)
previsoes

# COMPARANDO O RESULTADO
ytitanicTest

# CALCULANDO A PORCENTAGEM DE ACERTO
from sklearn.metrics import accuracy_score, confusion_matrix
accuracy_score(ytitanicTest, previsoes)

"""##**Árvore de Decisão - 80,86%**"""

# REALIZANDO O TREINAMENTO DO ALGORITMO
from sklearn.tree import DecisionTreeClassifier

arvoreTitanic = DecisionTreeClassifier(criterion = 'entropy', random_state=0)
arvoreTitanic.fit(xtitanicTrain, ytitanicTrain)

previsoes = arvoreTitanic.predict(xtitanicTest)
previsoes

accuracy_score(ytitanicTest, previsoes)

"""##**Random Forest - 81,57%**"""

from sklearn.ensemble import RandomForestClassifier

# TREINAMENTO COM O RANDOM FOREST
randomForestTitanic = RandomForestClassifier(n_estimators=40, criterion='entropy', random_state=0)
randomForestTitanic.fit(xtitanicTrain, ytitanicTrain)

previsoes = randomForestTitanic.predict(xtitanicTest)
previsoes

accuracy_score(ytitanicTest, previsoes)

"""##**Vizinho Mais Próximo (KNN) - 77,75%**"""

from sklearn.neighbors import KNeighborsClassifier

# CRIANDO A VARIÁVEL KNN E CONFIGURANDO OS PADRÕES CONFORME DOCUMENTAÇÃO
# ELE NÃO FAZ OS TREINAMENTOS, APENAS RECEBE AS VARÍAVEIS
knnTitanic = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
knnTitanic.fit(xtitanicTrain, ytitanicTrain)

previsoes = knnTitanic.predict(xtitanicTest)
previsoes

accuracy_score(ytitanicTest,previsoes)

"""##**Máquina de Vetores de Suporte (SVM) - 63,15%**"""

from sklearn.svm import SVC

# TREINANDO MODELO SVM
svmTitanic = SVC(kernel='rbf', random_state=1, C=1.0)
svmTitanic.fit(xtitanicTrain,ytitanicTrain)

previsoes = svmTitanic.predict(xtitanicTest)
previsoes

accuracy_score(ytitanicTest, previsoes)

"""##**Naive Bayes - 99,76%** """

from sklearn.naive_bayes import GaussianNB
naive = GaussianNB()
naive.fit(xtitanicTrain, ytitanicTrain)

previsaoNaive = naive.predict(xtitanicTest)
previsaoNaive

# Calculando a taxa de acerto 
accuracy_score(ytitanicTest, previsaoNaive)

# Matriz de confusão
cm = ConfusionMatrix(naive)
cm.fit(xtitanicTrain,ytitanicTrain)
cm.score(xtitanicTest, ytitanicTest)

"""#Probabilidade

Vou testas minha probabilidade de sair vivo do Titanic
"""

classe=int(input('Informe a classe de sua passsagem: '))
sexo=int(input('Informe o seu Gênero - (1) Masculino e (0) Feminino: '))
idade=int(input('Informe sua idade em anos: '))

probabilidade = naive.predict_proba([[classe,sexo,idade]])
probSobreviver= round(probabilidade[:,1][0]*100,2)

print('Sua probabilidade de sobrevivência ao Titanic seria de aproximadamente ----->',probSobreviver,'%')

"""Vish... minhas probabilidades são baixas eim...
Vamos ver a do meu irmão que já é um cara cheio da grana hehe
"""

classe=int(input('Informe a classe de sua passsagem: '))
sexo=int(input('Informe o seu Gênero - (1) Masculino e (0) Feminino: '))
idade=int(input('Informe sua idade em anos: '))

probabilidade = naive.predict_proba([[classe,sexo,idade]])
probSobreviver= round(probabilidade[:,1][0]*100,2)

print('Sua probabilidade de sobrevivência ao Titanic seria de aproximadamente ----->',probSobreviver,'%')

"""Só de estar na 1º classe a probabilidade dele é mais alta.E se for uma mulher,será que a probabilidade é maior?!"""

classe=int(input('Informe a classe de sua passsagem: '))
sexo=int(input('Informe o seu Gênero - (1) Masculino e (0) Feminino: '))
idade=int(input('Informe sua idade em anos: '))

probabilidade = naive.predict_proba([[classe,sexo,idade]])
probSobreviver= round(probabilidade[:,1][0]*100,2)

print('Sua probabilidade de sobrevivência ao Titanic seria de aproximadamente ----->',probSobreviver,'%')

"""É... acho que para sair vivo do Titanic eu deveria colocar uma peruca rs"""