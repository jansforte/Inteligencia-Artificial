#Author: JOHAN SEBASTIAN FUENTES ORTEA
#Date: 12/03/2021
#INGENIERÍA DE SISTEMAS - UCEVA

'''
Solución del Error:
El error simplemente constaba de 2 cosas:
	-Habia que instalar la librería de scipy
	-no tenía importado la librería numpy	
'''
'''--------------------------------------'''
from scipy import ndimage 							# Se importa ndimage de scipy.
import numpy as np 									#Importamos numpy le asignamos np como identificador de la librería.
import matplotlib.pyplot as plt 					#Importamos matplotlib.pyplot asignandole plt como identificador.

im = np.zeros((256, 256))							#Creamos una matriz de 256x256 y la llenamos de zeros
im[64:-64, 64:-64] = 1								#Recorremos la matrix desde 64 hasta -64 y las llenamos de 1.

im = ndimage.rotate(im, 15, mode='constant')		#Rotamos la imagen (matriz) 15 gradados y los campos que se 
													#superponen más allá del tamaño de la matriz serán constantes con mismo valor.

im = ndimage.gaussian_filter(im, 8)					#Aplicamos el filtro gausiano con un escalar de 8.

sx = ndimage.sobel(im, axis=0, mode='constant')		#Asignamos a sx el filtro sobel al eje 0 de la imagen y los campos que se 
													#superponen más allá del tamaño de la matriz serán constantes con mismo valor.

sy = ndimage.sobel(im, axis=1, mode='constant')		#Asignamos a sy  el filtro sobel al eje 1 de la imagen y los campos que se 
													#superponen más allá del tamaño de la matriz serán constantes con mismo valor.

sob = np.hypot(sx, sy)								#Asignamos a sob el valor de la hipotenusa obtenida por la raíz cuadrada de la
													#suma de los cuadrados de sx y sy.

plt.figure(figsize=(16, 5))							#Hacemos asignamos el tamaño de la ventana con ancho 16 y alto 5, medidas en pulgadas.
plt.subplot(141)									#Se hace un lienzo de 1 fila y 4 columnas y se trabajara en la columna 1.
plt.imshow(im, cmap=plt.cm.gray)					#Pintamos la imagen im aplicandole un color mapeado gris .
plt.axis('off')										#No mostramos los ejes.
plt.title('square', fontsize=20)					#Asignamos el titulos sqquare de tamaño 20.
plt.subplot(142)									#En el lienzo hecho de 1 fila y 4 columnas, apuntamos la columna 2 para trabajar.
plt.imshow(sx)										#Pintamos la imagen sx.
plt.axis('off')										#No mostramos los ejes.
plt.title('Sobel (x direction)', fontsize=20)		#Asignamos el título con un tamaño 20.
plt.subplot(143)									#En el lienzo hecho de 1 fila y 4 columnas, apuntamos la columna 3 para trabajar.
plt.imshow(sob)										#Pintamos la imagen sob.
plt.axis('off')										#No mostramos ejes.
plt.title('Sobel filter', fontsize=20)				#Asignamos un titulo con tamaño 20.

im += 0.07*np.random.random(im.shape)				#Sumamos a la matriz im el resultado de la multiplicación de 0.07 con un valor
													#random obtenida de por el tamaños de la figura de la matriz im.

sx = ndimage.sobel(im, axis=0, mode='constant')		#Reasignamos a sx el filtro sobel al eje 0 de la imagen y los campos que se 
													#superponen más allá del tamaño de la matriz serán constantes con mismo valor.

sy = ndimage.sobel(im, axis=1, mode='constant')		#Reasignamos a sy el filtro sobel al eje 1 de la imagen y los campos que se 
													#superponen más allá del tamaño de la matriz serán constantes con mismo valor.

sob = np.hypot(sx, sy)								#Reasignamos a sob el valor de la hipotenusa obtenida por la raíz cuadrada de la
													#suma de los cuadrados de sx y sy.

plt.subplot(144)									#Ahora indicamos que trabajaremos en la columna 4 del subplot de 1 fila y 4 columndas.
plt.imshow(sob)										#Pintamos la imagen sob.
plt.axis('off')										#Ocultamos los ejes.
plt.title('Sobel for noisy image', fontsize=20)		#Asignamos un título con un tamaño de 20.



plt.subplots_adjust(wspace=0.02, hspace=0.02, top=1, bottom=0, left=0, right=0.9) 
													#Se ajusta el subplot con margenes y espaciado entre columnas

plt.show()											#Mostramos la ventana