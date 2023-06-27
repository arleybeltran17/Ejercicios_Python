#Determinar Si Un Elemento Se Repite En Otra Lista

# Definimos una funcion
def repetido(lista1, lista2):

#Convertimos las listas en cojuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

#realizamos una interseccion 
    elementos_repetidos = conjunto1.intersection(conjunto2)

#el resultado de esa interseccion la convertimos en una lista
    lista_repetidos = list(elementos_repetidos)

#retornamos la lista de elementos repetidos
    return lista_repetidos

#creamos las 2 listas en este caso se repiten los numeros 4 y 5
lista1 = [1, 2, 3, 4, 5,9]
lista2 = [4, 5, 6, 7, 8,0]

#llamamos a la variable de los elementos repetidos y le decimos que sea igual a la funcion que contiene las 2 listas
elementos_repetidos = repetido(lista1, lista2)

#por ultimo Imprimimos el resultado
print("Elementos repetidos:", elementos_repetidos)