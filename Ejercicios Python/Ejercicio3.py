# Calcular Si Una Cadena De Caracteres Tiene Mas De 2 Vocales

#Definimos Una Funcion La Cual Tenga En Cuenta La Cadena De Caracteres

def vocales(cadena):

    #Creamos Un Contador Para Que Valla Contando Cuantas Vocales Tiene La Cadena De Caracteres
    contador = 0
    # Creamos Una Variable Para Especificar Las Vocales Tanto En Mayusculas Como En Minusculas
    vocales = "aeiouAEIOU"
    
    #Creamos Un For Que Tenga En Cuenta La Longitud De La Cadena 
    for caracter in cadena:
        #Y Una Condicion La Cual Si Encuentra Una Vocal Valla Sumando De A Uno Al Contador 
        if caracter in vocales:
            contador += 1
            #Creamos Otra Condicion La Cual Se Le Dice Que Si El Contador Es Mayor O Igual A 2 Retorne True Si No Retorne False
            if contador >= 2:
                return True
    
    return False

#Creamos Otra Funcion En La Cual Tenga En Cuenta Los Elementos De La Lista
def cadena_vocales(lista):
    for elemento in lista:
        #Llamamos A La Funcion De Las Vocales Para Que Calcule Las Vocales Que Halla En Cada Cadena
        #Si Se Cumple La Condicion Retorne El Elemento En El Cual Se Encuentran Mas De 2 Vocales Si No Retorne No Existe
        if vocales(elemento):
            return elemento
    
    return "No existe"

# Creamos Una Lista Y Una Variable De Resultado, La Cual Llama A La Funcion De cadena_vocales Y Por Ultimo Se Imprime El Resultado
mi_lista = ["hola", "mundo", "Python", "amigo"]
resultado = cadena_vocales(mi_lista)
print("Cadena con dos o más vocales:", resultado)
#Tener En Cuenta Que Solo Imprime El Primer Valor Que Cumpla Con La Condicion De 2 o Mas Vocales