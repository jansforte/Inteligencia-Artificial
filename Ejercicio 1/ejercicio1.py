import numpy as np

from matplotlib import pyplot as dibujar
edad = np.array([23, 20, 22, 28, 21, 25, 25])

print ("Las edades son: ")
print (edad)

print ("El rango ptp es: ",np.ptp(edad))

Q1 = np.percentile(edad,25)
Q2 = np.percentile(edad,50)
Q3 = np.percentile(edad,75)

print ("Los tres cuartiles son: ")
print ("Q1 = ",Q1)
print ("Q2 = ",Q2)
print ("Q3 = ",Q3)

print ("La Mediana es: ",np.median(edad))
print ("La Media es: ",np.mean(edad))
print ("La Desviación estandar es: ",np.std(edad))

x = ['ptp','Q1(25%)','Q2(50%)','Q3(75%)','Mediana','Media', 'D.Estandar']
y = [np.ptp(edad),Q1,Q2,Q3,np.median(edad),np.mean(edad),np.std(edad)]

dibujar.bar(x, y, align = 'center')
dibujar.title('Valores estadísticos de edades')
dibujar.ylabel('Resultados')
dibujar.xlabel('Atributos')
dibujar.show()
