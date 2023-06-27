# Definir Si Existe Una Cadena De Caracteres Sea Palindrimo

# Definimos una Funcion
def palindromo(cadena):
    
    # Eliminamos Espacion Y Convetimos En Mayusculas Con Los Metodos Replace Y Lower
    cadena = cadena.replace(" ", "").lower()
    
    # Verificar Si La Cadena Puesta Es Un Palindromo Con El Metodo slicing Ya Que Comparamos La Cadena Al Derecho Y Al Reves
    if cadena == cadena[::-1]:
        return True
    else:
        return False

# Definimos Otra Funcion Que Tenga En Cuenta Una Lista y Creamos Un
# For Que Tenga En Cuenta Los Elementos Dentro De Una Lista
# Luego Se Crea Un Condicional En El Cual Llamamos A La Primera Funcion
# La Cual Analiza Cada Cadena De Caracteres Y Devuelve La Que Se Lea Tanto Al Derecho Como Al Reves
# Si No Encuentra Ninguna Entonces Retorna No Existe
def encontrar_cadena(lista):
    for elemento in lista:
        if palindromo(elemento):
            return elemento
    return "No existe"

# Creamos Una Lista Con Diferentes Cadenas De Caracteres, La Cual Solo Imprimira Reconocer
# Si Quitamos Reconocer Imprimira No Existe
mi_lista = ["casa", "reconocer", "hola"]
resultado = encontrar_cadena(mi_lista)
print("Cadena palíndrome:", resultado)