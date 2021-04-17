import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sb
 
#%matplotlib inline
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
 
from sklearn.model_selection import train_test_split
#from sklearn.metrics import classification_report #Cree un informe de texto que muestre las principales métricas de clasificación.
#from sklearn.metrics import confusion_matrix #Calcule la matriz de confusión para evaluar la precisión de una clasificación.
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest


dataframe = pd.read_csv(r"comprar_alquilar.csv")
print(dataframe.head(10))

print(dataframe.groupby('comprar').size())

dataframe.drop(['comprar'], axis=1).hist()
plt.show()

dataframe['gastos']=(dataframe['gastos_comunes']+dataframe['gastos_otros']+dataframe['pago_coche'])
dataframe['financiar']=dataframe['vivienda']-dataframe['ahorros']
print(dataframe.drop(['gastos_comunes','gastos_otros','pago_coche'], axis=1).head(10))


reduced = dataframe.drop(['gastos_comunes','gastos_otros','pago_coche'], axis=1)
print(reduced.describe())

X=dataframe.drop(['comprar'], axis=1)
y=dataframe['comprar']

#Seleccione características de acuerdo con las k puntuaciones más altas.
best=SelectKBest(k=5)

#Ajusta el transformador a X e y con parámetros opcionales fit_params y devuelve una versión transformada de X
X_new = best.fit_transform(X, y)

print(X_new.shape) #devuelve una tupla con el tamaño del array, pero puede ser también usado para redimensionarlo

#Un índice que selecciona las características retenidas de un vector de características
#al ser true esta es una matriz entera que devuelve las columnas que hacen parte de los 5 mejores datos
selected = best.get_support(indices=True)
print(selected)
print(X.columns[selected])

used_features =X.columns[selected]

#Esto cambia el mapa de colores predeterminado, así como el mapa de colores de la imagen actual, si hay uno.
colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)

#Trace datos rectangulares como una matriz codificada por colores.
#corr() Calcule la correlación de columnas por pares, excluyendo NA / valores nulos.
sb.heatmap(dataframe[used_features].astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)


# Split dataset in training and test datasets
#Divide las matrices en subconjuntos de prueba, el test_size 
#recibe un parametro flotante o entero, si es flotante será de 0.0 a 1.0, y 
#representan la proporción del conjunto de datos para incluir en la división de prueba.
#mientras que el random_state Controla la mezcla aplicada a los datos antes de aplicar la división.
X_train, X_test = train_test_split(dataframe, test_size=0.2, random_state=6) 
y_train =X_train["comprar"]
y_test = X_test["comprar"]

# Instantiate the classifier
gnb = GaussianNB()

# Entrenador del algoritmo, recibe 2 parametros, x y y
# x =Vectores de entrenamiento, donde n_samples es el 
# número de muestras y n_features es el número de características
# y = son los valores objetivo 
gnb.fit(
    X_train[used_features].values,
    y_train
)

#Realizar clasificación en una matriz de vectores de prueba con respecto al valor objetivo
y_pred = gnb.predict(X_test[used_features]) 


#el score Devuelve la precisión media en los datos de prueba y las etiquetas dados.
# el .2f es para que me redonde el dato
print('Precisión en el set de Entrenamiento: {:.2f}'
     .format(gnb.score(X_train[used_features], y_train)))
print('Precisión en el set de Test: {:.2f}'
     .format(gnb.score(X_test[used_features], y_test)))


#                 ['ingresos', 'ahorros', 'hijos', 'trabajo', 'financiar']
print(gnb.predict([[2000,        5000,     0,       5,         200000],
                   [6000,        34000,    2,       5,         320000] ]))
#Resultado esperado 0-Alquilar, 1-Comprar casa

wait = input("PRESS ENTER TO CONTINUE.")