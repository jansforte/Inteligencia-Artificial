"""Spelling Corrector in Python 3; see http://norvig.com/spell-correct.html

Copyright (c) 2007-2016 Peter Norvig
MIT license: www.opensource.org/licenses/mit-license.php
"""

################ Spelling Corrector 

#importamos la librería re para manejar expresiones regulares
import re
#Importamos la librería de pandas para la lectura de el archivo CREA_TOTAL.txt
import pandas as pd

#Creamos un dataframe que almacenará los datos en columnas y filas obtenidos del archivo 
df = pd.read_csv('CREA_total.TXT', sep='\t', encoding='latin-1',low_memory=False)
#Renombramos las columnas
df.columns = ['palabra','frecuenciaAbsoluta','frecuenciaNormalizada']
#Eliminamos la columna frecuenciaNormalizada debido a que no la usaremos
df = df.drop(['frecuenciaNormalizada'], axis=1)
#Limpiamos los datos de la columna palabra para eliminar espacios
df['palabra'] = df['palabra'].str.replace(' ','')
#Limpiamos los datos de la columna frecuencia absoluta para eliminar las comas
df['frecuenciaAbsoluta'] = df['frecuenciaAbsoluta'].str.replace(',','')
#Convertimos el dato a tipo numerico
df['frecuenciaAbsoluta'] = pd.to_numeric(df['frecuenciaAbsoluta'])
#Creamos el diccionario de datos pasando la columna palabra como clave y la columna frecuenciaAbsoluta como su valor
d1 = dict(zip(df['palabra'],df['frecuenciaAbsoluta']))
#asignamos el diccionario de datos a la variable WORDS
WORDS = d1 

#se define la función P que tomará la palabra y la suma de todos los valores que estan en el diccionario
def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    #retornamos la probabilidad de la palabra
    return WORDS[word] / N

#se define la funcion correction que convertira la palabra obtenida a minuscula y retornara la palabra que
#posiblemente es la que se quería retornar a partir de la maxima frecuencia obtenida por la funcion p
def correction(word): 
    "Most probable spelling correction for word."
    word = word.lower()
    #llama la funcion candidatos para procesar la palabra escrita
    return max(candidates(word), key=P)

#la funcion candidatos recibe la palabra que le pasa correction y llama las funciones respectivas para
#retornar una lista de palabras que son candidatos a ser iguales a esta
def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

#La funcion know busca la palabra para verificar que exista en el diccionario de datos, de existir, la retorna como
#un conjunto o lista
def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

#La funcion edits1 retorna una lista de palabras candidatas que surgen a partir de una alteración de la palabra original
def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnñopqrstuvwxyz'
    #me hace una matriz que separa las letras de las palabras
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    #una vez realizado el split el me genera una lista de palabras que surgen al eliminar cada letra
    deletes    = [L + R[1:]               for L, R in splits if R]
    #transposes es una lista que con la transpocisión de las letras de la palabra y me genera una lista de estas
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    #el replace es una lista que toma el alfabeto y remplaza cada letra de la palabra (una a la vez) con una del alfabeto hasta completarse el alfabeto
    #esta la lista (gran lista debido a que por cada letra de la palabra se cambia a la letra del alfabeto) 
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    #el inserts es una lista con las letras del alfabeto insertadas en la palabra, ya sea al inicio, al final o entre letras.
    inserts    = [L + c + R               for L, R in splits for c in letters]
    #luego se retorna un conjunto de listas concatenadas
    return set(deletes + transposes + replaces + inserts)

#La función edits2 usa edits1 para usar la lista obtenida y alterarlas nuevamente para generar nuevas palabras
#luego retorna esa lista.
def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

################ Test Code 

#La función unit_test se encarga de testear que todo esté funcionando correctamente
#debido a que estoy usando diccionario de datos en español no funcionará el assert
#porque está para el crepus en ingles, pero conocemos su funcionamiento y su importancia
def unit_tests():
    assert correction('speling') == 'spelling'              # insert
    assert correction('korrectud') == 'corrected'           # replace 2
    assert correction('bycycle') == 'bicycle'               # replace
    assert correction('inconvient') == 'inconvenient'       # insert 2
    assert correction('arrainged') == 'arranged'            # delete
    assert correction('peotry') =='poetry'                  # transpose
    assert correction('peotryy') =='poetry'                 # transpose + delete
    assert correction('word') == 'word'                     # known
    assert correction('quintessential') == 'quintessential' # unknown
    assert words('This is a TEST.') == ['this', 'is', 'a', 'test']
    assert Counter(words('This is a test. 123; A TEST this is.')) == (
           Counter({'123': 1, 'a': 2, 'is': 2, 'test': 2, 'this': 2}))
    assert len(WORDS) == 32198
    assert sum(WORDS.values()) == 1115585
    assert WORDS.most_common(10) == [
     ('the', 79809),
     ('of', 40024),
     ('and', 38312),
     ('to', 28765),
     ('in', 22023),
     ('a', 21124),
     ('that', 12512),
     ('he', 12401),
     ('was', 11410),
     ('it', 10681)]
    assert WORDS['the'] == 79809
    assert P('quintessential') == 0
    assert 0.07 < P('the') < 0.08
    return 'unit_tests pass'

#La funcion spelltests es para verificar la eficiencia del algoritmo con respecto 
#a los archivos en ingles que manejaron en el proyecto del programa.
def spelltest(tests, verbose=False):
    "Run correction(wrong) on all (right, wrong) pairs; report results."
    import time
    start = time.perf_counter()
    good, unknown = 0, 0
    n = len(tests)
    for right, wrong in tests:
        w = correction(wrong)
        good += (w == right)
        if w != right:
            unknown += (right not in WORDS)
            if verbose:
                print('correction({}) => {} ({}); expected {} ({})'
                      .format(wrong, w, WORDS[w], right, WORDS[right]))
    dt = time.perf_counter() - start
    print('{:.0%} of {} correct ({:.0%} unknown) at {:.0f} words per second '
          .format(good / n, n, unknown / n, n / dt))


def Testset(lines):
    "Parse 'right: wrong1 wrong2' lines into [('right', 'wrong1'), ('right', 'wrong2')] pairs."
    return [(right, wrong)
            for (right, wrongs) in (line.split(':') for line in lines)
            for wrong in wrongs.split()]

#if __name__ == '__main__':
    #print(unit_tests())
#spelltest(Testset(open('spell-testset1.txt')))
#spelltest(Testset(open('spell-testset2.txt')))

#imprimimos la corrección de la palabra
print(known(['jolatallll']))
if len(candidates('jolatallll'))==1 :
	vacio = set()
	if vacio == known(['jolatallll']):
		print("Esta vacio")