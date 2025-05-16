"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    nombre = "files/input/data.csv"
    
    
    sumas_columna_5 = {}
    
    archivo = open(nombre, "r")

    for linea in archivo:
        linea_limpia = linea.strip()
        
 
        columnas = linea_limpia.split('\t')
        
        letra_clave = columnas[0]
        
        cadena_col5 = columnas[4] 
        
 
        suma_valores_linea_actual = 0
        
        pares_individuales = cadena_col5.split(',') 
        
        for par in pares_individuales:
            
            
            partes_del_par = par.split(':')
            
            valor_numerico_del_par = int(partes_del_par[1])
            
            suma_valores_linea_actual += valor_numerico_del_par
     
        sumas_columna_5[letra_clave] = sumas_columna_5.get(letra_clave, 0) + suma_valores_linea_actual
            
    archivo.close()
    
    lista_de_tuplas = list(sumas_columna_5.items())
    
    tuplas_ordenadas = sorted(lista_de_tuplas)
    
    diccionario_resultado = {}
    for clave, suma in tuplas_ordenadas:
        diccionario_resultado[clave] = suma
        
    return diccionario_resultado

