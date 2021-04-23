# Importar la libreria Pandas para manejar datasets
import pandas as pd

# Importar el contador de vectorizacion de la librería sklearn
from sklearn.feature_extraction.text import CountVectorizer

# Importamos train_test_split desde la librería sklearn con el fin de poder dividir los datos en conjunto de entrenamiento y de test
from sklearn.model_selection import train_test_split

# Importamos MultinomialNB desde la librería sklear con el fin de clasificar de características discretas
from sklearn.naive_bayes import MultinomialNB

# Importamos de la librería sklearn con el fin de evaluar la exactitud, precisión, sensibilidad y el promedio ponderado de la precision y la sensibilidad 
# de nuestro algoritmo
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Descargamos el smsspamcollection.zip del Dataset de  https://archive.ics.uci.edu/ml/machine-learning-databases/00228/
# Lo descomprimimos en la mis carpeta de este archivo
df = pd.read_table('smsspamcollection/SMSSpamCollection', 
                   sep='\t', 
                   names=['label','sms_message'])
# Visualización de las 5 primeras filas
print(df.head())

# Conversion
df['label'] = df.label.map({'ham':0, 'spam':1})
# Visualizar las dimensiones de los datos
print(df.shape)

# Obtenemos del dataset los datos de la columna sms_message para entrenamiento y prueba, lo mismo con label.
X_train, X_test, y_train, y_test = train_test_split(df['sms_message'], df['label'], random_state=1)
print('Numero de filas total del dataset: {}'.format(df.shape[0]))
print('Numero de filas del conjunto de entrenamiento: {}'.format(X_train.shape[0]))
print('Numero de filas del conjunto de testeo: {}'.format(X_test.shape[0]))

# Iniciamos el metodo CountVectorizer
count_vector = CountVectorizer()
# Ajustamos los datos de entrenamiento y devolvemos la matriz
training_data = count_vector.fit_transform(X_train)
# Transformamos los datos de prueba y retornamos la matriz. Los datos de prueba no se ajustan.
testing_data = count_vector.transform(X_test)

# Inicializamos el metodo MultinomialNB
naive_bayes = MultinomialNB()
# Ajustamos los datos de entreenamiento en clasificador para entrenar nuestro algoritmo
naive_bayes.fit(training_data, y_train)
# Realizamos la predicción con nuestros datos de prueba y el resultado lo almacenamos en la variable predictions
predictions = naive_bayes.predict(testing_data)

# los valores retronan un flotaten entre 0 - 1 siendo 1 el mejor puntaje
print('Exactitud: ', format(accuracy_score(y_test, predictions)))
print('Precisión: ', format(precision_score(y_test, predictions)))
print('Sensibilidad: ', format(recall_score(y_test, predictions)))

# Promedio ponderado de la presición y sensibilidad de nuestro algoritmo
print('F1: ', format(f1_score(y_test, predictions)))