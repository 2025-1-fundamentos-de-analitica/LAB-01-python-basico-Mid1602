"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    nombre_del_archivo = "files/input/data.csv"
    
   
    sumas_por_letra = {}
    
    archivo = open(nombre_del_archivo, "r")

    for lineas in archivo:
        linea_limpia = lineas.strip()
        
       
        columnas = linea_limpia.split('\t')
        
        valor_a_sumar = int(columnas[1])
        
        cadena_letras = columnas[3] 
        
        letras_individuales = cadena_letras.split(',') 
        
        for letra in letras_individuales:
            
            sumas_por_letra[letra] = sumas_por_letra.get(letra, 0) + valor_a_sumar
            
    archivo.close()
    
    
    lista_de_tuplas = list(sumas_por_letra.items())
    
    tuplas_ordenadas = sorted(lista_de_tuplas)
    
    
    diccionario_resultado = {}
    for clave_letra, suma_valor in tuplas_ordenadas:
        diccionario_resultado[clave_letra] = suma_valor
        
    return diccionario_resultado


