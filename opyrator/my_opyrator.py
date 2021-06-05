##
##Athor: JOHAN SEBASTIAN FUENTES ORTEGA - JEISON ANDRES FUENTES ORTEGA
##Usando la librería de opyrator
##
from pydantic import BaseModel
#implemento el codigo del spell
import spell as sp

class Input(BaseModel):
    message: str

class Output(BaseModel):
    message: str

def buscador(palabra):
	#recibo la palabra del navegador y la convierto en minuscula
	palabra = palabra.lower()
	#obtengo las palabras semejantes a la palabra
	conjunto = sp.candidates(palabra)
	
	#en caso tal de obtener una lista de una sola palabra verifico que exista
	#si no existe devuelvo un 0
	if len(conjunto) == 1 :
		vacio = set()
		if vacio == sp.known([palabra]):
			conjunto = "0"
	return conjunto

def hello_world(input: Input) -> Output:
    """Returns the `message` of the input data."""
    #print(sp.candidates(input.message))sp.candidates(input.message)
    return Output(message=" ".join(buscador(input.message)))