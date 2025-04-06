"""Crear una función de ordenamiento ascendente y descendente utilizando el archivo presentado en clase. 
Realicen las acciones necesarias para poder imitar el comportamiento de la función sort() y reverse() en cada caso.

Estas funciones se deben aplicar para arreglos:
Tipo list
Tipo np.array"""

import numpy as np

# Función auxiliar para clasificar los tipos
def tipo_ordenado(valor):
    if isinstance(valor, str):
        return (0, str(valor))
    elif isinstance(valor, float):
        return (1, float(valor))
    elif isinstance(valor, int):
        return (2, int(valor))
    elif isinstance(valor, bool):
        return (3, int(valor))  # Para que False < True
    else:
        return (4, str(valor))  # Otros tipos al final

class Estructura:
    def __init__ (self):
        self.arreglo = []
        self.arregloNP = np.array([], dtype=object)

    def insertar(self, valor):
        self.arreglo.append(valor)
        return self.arreglo

    def insertarNP(self, i, valor):
        tam = len(self.arregloNP)
        if 0 <= i <= tam:
            self.arregloNP = np.insert(self.arregloNP, i, valor)
        else:
            print("Índice no válido")
        return self.arregloNP

    def ordenar_lista(self, ascendente=True):
        self.arreglo.sort(key=tipo_ordenado, reverse=not ascendente)
        return self.arreglo

    def ordenar_np(self, ascendente=True):
        lista_convertida = list(self.arregloNP)
        lista_convertida.sort(key=tipo_ordenado, reverse=not ascendente)
        self.arregloNP = np.array(lista_convertida, dtype=object)
        return self.arregloNP
    
x = Estructura()
x.insertar(5)
x.insertar(1)
x.insertar(2)
x.insertar(9)

x.insertarNP(0, 4)
x.insertarNP(1, 2)
x.insertarNP(2, 3)
x.insertarNP(3, 6)

print("Original lista:", x.arreglo)
print("Original numpy:", x.arregloNP)

print("Lista ordenada ascendente:", x.ordenar_lista(True))
print("Lista ordenada descendente:", x.ordenar_lista(False))

print("Numpy ordenado ascendente:", x.ordenar_np(True))
print("Numpy ordenado descendente:", x.ordenar_np(False))