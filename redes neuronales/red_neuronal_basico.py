import numpy as np
from matplotlib import pyplot as plt

#función sigmoidea
def sigmoid(x):
    return 1/(1+np.exp(-x))

#Derivada de la sigmoidea
def sigmoid_der(x):
    return sigmoid(x)*(1-sigmoid(x))

#primero generamos aleatoriamente 100 puntos espaciados linealmente entre -10 y 10
input = np.linspace(-10, 10, 100)

#Dibujamos los valores de entrada en función de los valores sigmoidales, la marcamos de color rojo
plt.plot(input, sigmoid(input), c="r")
plt.show()

#Este es el conjunto de características original
feature_set = np.array([[0,1,0],[0,0,1],[1,0,0],[1,1,0],[1,1,1]])
#el label son los valores observaods, son los datos que definen que la persona tiene diabetes
labels = np.array([[1,0,0,1,1]]) 
#
labels = labels.reshape(5,1)

#el seed se aplica para obtener los mismos valores aleatorios cada vez que se ejecute este archivo
np.random.seed(42)
#genera una matriz de 3x1
weights = np.random.rand(3,1)
bias = np.random.rand(1)
#establecemos la tasa de aprendizaje en 5%
lr = 0.05

#aquí entrenamos el algoritmo de nuestros datos 20 mil veces
for epoch in range(20000):
    inputs = feature_set

    # feedforward step1
    #aquí se hace el producto punto del conjunto original con el peso + el sesgo para generar el escalar
    XW = np.dot(feature_set, weights) + bias

    #feedforward step2
    #se pasa el producto escalar para obtener la sigmoidea del algoritmo
    z = sigmoid(XW)


    # backpropagation step 1
    # encontramos el error al restarle las etiquetas a la sigmoidea
    error = z - labels

    #aqui vemos como va mermando el error
    print(error.sum())

    # backpropagation step 2
    #al realizar la derivada da 2(z-labels), el 2 al ser constante se ovbia
    #quedando tal que la derivada del cost respecto derivada predicha es el error
    dcost_dpred = error
    #la derivada predicha respecto a la derivada sigmoidea será la derivada de la sigmoidea
    dpred_dz = sigmoid_der(z)

    #el producto de la derevida del costo en funcion de lo predicho por la derivada de
    #el predicho respecto a la derivada sigmoidea
    z_delta = dcost_dpred * dpred_dz
    #Realizamos la transpuesta de los conjuntos originales
    inputs = feature_set.T
    #multiplicamos la variable de aprendizaje por de la transpuesta de nuestros datos originales
    #y el z_delta
    #nos da los pesos, y al multiplicar por la variable de aprendizaje hacemos que aumente
    #la velocidad de la convergencia
    weights -= lr * np.dot(inputs, z_delta)

    #por último calculamos el bias (b) para tener la funcion: z=x1w1+x2w2+x3w3+b
    for num in z_delta:
        bias -= lr * num

#predecimos el valor en el caso que una persona fuma, para hayar la probabilidad de que tenga diabetes o no
single_point = np.array([1,0,0])
#hayamos la sigmoidea del producto punto de nuestra persona con el peso que se calculó y le sumamos el bias
result = sigmoid(np.dot(single_point, weights) + bias)
#por pultimo mostramos la probabilidad de tener o no diabetes
print(result)

single_point = np.array([0,1,0])
result = sigmoid(np.dot(single_point, weights) + bias)
print(result)