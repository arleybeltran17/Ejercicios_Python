#Calcular Elementos Que Existen En La Primera Lista Pero En La Segunda No

# Creamos Una Funcion La Cual Contenga Las 2 Listas
def Faltantes(lista1, lista2):
    #Llamamos Una Variable De Faltantes
    Faltantes = []
    
    #Creamos un ciclo el cual tenga en cuenta los elementos de la primera lista
    for elemento in lista1:
        #Se Crea Una Condicion En La Cual Verifique Los Elementos Faltantes De La Segunda Lista
        if elemento not in lista2:
            #El Elemento Flatante Se Agrega  nuestra Lista De Faltantes Con Un Append 
            Faltantes.append(elemento)
    #Retorna Los Elementos Faltantes
    return Faltantes
#Creamos Las 2 Listas 
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
#Creamos Una Variable De Resultado En La Cual Le Decimos Que Sea Igual A La Funcion De Faltantes 
resultado = Faltantes(lista1, lista2)
#Por Ultimo Imprimimos El Resultado En Este Caso En La Lista 2 Flatan Los Elementos 1 ,2 y 3
print("Elementos que no están en la segunda lista:", resultado)