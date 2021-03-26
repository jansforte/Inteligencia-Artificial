#Author: JOHAN SEBASTIAN FUENTES ORTEA
#Date: 12/03/2021
#INGENIERÍA DE SISTEMAS - UCEVA

#Practices 1:
"""
Consider a vector of email addresses scraped from the internet:
robert ‘dot’ colautti ‘at’ queensu ‘dot’ ca
chris.eckert[at]queensu.ca
lonnie.aarssen at queensu.ca
"""
import re
print("Solucion Ejercicio 1:")
e1 = re.sub("( 'at' )",'@',"robert 'dot' colautti 'at' queensu 'dot' ca")
e1 = re.sub("( 'dot' )",".",e1)
print("1) "+e1)

e2 = re.sub("(\\[at])",'@',"chris.eckert[at]queensu.ca")
print("2) "+e2)

e3 = re.sub("( at )","@","lonnie.aarssen at queensu.ca")
print("3) "+e3)
print()
print("Solucion Ejercicio 2:")

MySeq="ATGTGTGATAGATATAGTTTATAG"
print("Original: "+MySeq)
e4 = re.sub("T","U",MySeq)
print("Modifica: "+e4)
e5 = re.split("UGA",e4)
print(e5)