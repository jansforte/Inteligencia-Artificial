#Nombre: JOHAN SEBASTIAN FUENTES ORTEGA Y JEISON ANDRES FUENTES ORTEGA
#importamos las librerias para manejar dataset y el uso del analisis discriminante lineal
from sklearn.datasets import load_wine
import pandas as pd
import numpy as np
#hacemos que los datos tengan una precision de 4 digitos decimales
np.set_printoptions(precision=4)
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

"""
Los datos son el resultado de un análisis químico de vinos cultivados en la misma 
región en Italia por tres cultivadores diferentes. Se toman trece medidas diferentes 
para los diferentes componentes que se encuentran en los tres tipos de vino.
"""
#cargamos el dataset de los vinos brindados por la librería sklearn
wine = load_wine()
#usamos panda para crear un dataset seleccionando como columnas las características de los vinos
X = pd.DataFrame(wine.data, columns=wine.feature_names)
#imprimimos el tamaño de la matriz
print(X.shape)
#imprimimos las 5 primeras filas
print(X.head())
#asignamos a y los tipos de vino 
y = wine.target

#inicializamos un analisis linear discriminante
lda = LinearDiscriminantAnalysis()
#realizamos la transformación y clasificación respecto a las características y el tipo de vino
X_lda = lda.fit_transform(X, y)

#mostramos los resultados de la varianza
print(lda.explained_variance_ratio_)

#asigno el nombre al eje x
plt.xlabel('LD1')
#asigno el nombre al eje y
plt.ylabel('LD2')
#graficamos los datos
plt.scatter(
    X_lda[:,0],
    X_lda[:,1],
    c=y,
    cmap='rainbow',
    alpha=0.7,
    edgecolors='b'
)
plt.show()

#entrenamos la inteligencia
X_train, X_test, y_train, y_test = train_test_split(X_lda, y, random_state=1)
#inicializamos el arbol que clasificara las decisiones
dt = DecisionTreeClassifier()
#realizamos el proceso de aprendizaje
dt.fit(X_train, y_train)
#tomamos los datos a predecir
y_pred = dt.predict(X_test)
#generamos la matriz de confución que me retornará la matriz con la clasificación de los vinos
print(confusion_matrix(y_test, y_pred))