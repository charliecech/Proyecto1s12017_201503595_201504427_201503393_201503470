import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./')
#Importo la Clase
from nodos import Claseuno
class ClaseListaPila(Claseuno):
	 def __init__(self):
	 	 self.primerNodo = None
	 	 self.ultimoNodo = None

	 def estaVacia(self):
	 	if self.primerNodo == None:
	 		print "si esta vacia"
	 		return True
	 	return False
	 def push(self,datos):
	 	if self.estaVacia():
	 		 #print "insertar primer elemento en la lista"
	 		 self.ultimoNodo = Claseuno(datos,None)
	 		 self.primerNodo = self.ultimoNodo
	  	else:
	  		 #print "existen elementos en la lista"
	  	     self.primerNodo = Claseuno(datos,self.primerNodo)
	 def pop(self):
	 	if self.estaVacia():
	 		return "Esta vacia"
	 	else:
	 		data = self.primerNodo.datos
	 		self.primerNodo = self.primerNodo.nodo
	 		return data
	 def mostrar(self):
	 	 actual = self.primerNodo
	 	 while (actual != None):
	 	 	print "Dato: " + actual.datos
	 	 	actual = actual.nodo
	 	 print "Fin"

	 	
	  		     
	 	