import os
from markovbot import MarkovBot

# Initialise a MarkovBot instance
print("-----------------------------------------------------------")
print("Initialising MarkovBot ...")
tweetbot = MarkovBot()

#os.path.abspath(__file__) me retorna la ruta de este archivo
#que al aplicarle os.path.dirname, me retorna la ubicacion del archivo
dirname = os.path.dirname(os.path.abspath(__file__))

print("-----------------------------")
print("Getting the path ...")
# Construct the path to the book
#os.path.join me concatena la ubicación del archivo con el nombre del archivo que se va a leer
book = os.path.join(dirname, u'DonQuijote.txt')

# Make your bot read the book!
print("-----------------------------")
print("Reading the book ...")
#read es un funcion de la libreria os,
#esta metodo es aplicada en markovbot35 en mi caso.
#para poder usar el read, primero se debe abrir el archivo
#por eso se usa el metodo open, metodo que si no recibe el parametro
#encoding='utf-8' leerá el archivo con el encoding mbcs, encoding standar de python.
#por otro lado el bot lee el archivo y guardará lo que aprende en la base de datos que nosotros
#asignemos, en este caso spanish, esta base de datos se crea, si no pasamos el parametro, usara una
#base de datos por defecto
tweetbot.read(book, database='spanish')

print("-----------------------------")
print("Generating the text ...")
#my_first_text = tweetbot.generate_text(50, seedword=['dream', 'psychoanalysis'])

#una vez que el bot haya aprendido, se llama al metodo generate_text para que me genere un texto,
#le decimos que lo genere con 50 palabras, que use la base de datos donde almacena lo que aprendió,
#y le pasamos los parametros que queremos que hable en este caso de sancho o rocinante.
my_first_text = tweetbot.generate_text(50, database='spanish',seedword=[u'Sancho', u'Rocinante'])
print("tweetbot says:")
print(my_first_text)

print("")
print("-----------------------------")
print("")
print("Generating the text ...")
#my_first_text = tweetbot.generate_text(50, seedword=['dream', 'psychoanalysis'])
my_first_text = tweetbot.generate_text(50, database='spanish', seedword=[u'Sancho', u'Rocinante'])
print("tweetbot says:")
print(my_first_text)

print("")
print("-----------------------------")
print("")
print("Generating the text ...")
#my_first_text = tweetbot.generate_text(50, seedword=['dream', 'psychoanalysis'])
my_first_text = tweetbot.generate_text(50, database='spanish', seedword=[u'Sancho', u'Rocinante'])
print("tweetbot says:")
print(my_first_text)