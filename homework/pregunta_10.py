"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    nombre_del_archivo = "files/input/data.csv"
    
    lista = []
    
    archivo = open(nombre_del_archivo, "r")

    for linea in archivo:
        linea_limpia = linea.strip()
        
        
        columnas = linea_limpia.split('\t')
       
        letra = columnas[0]
        
        
        columna_4 = columnas[3]
        
        elementos_col_4 = columna_4.split(',')
        cantidad_col_4 = len(elementos_col_4)
        
        columna_5 = columnas[4] 
        
        elementos_col_5 = columna_5.split(',')
        cantidad_col_5 = len(elementos_col_5)
        
        tupla_actual = (letra, cantidad_col_4, cantidad_col_5)
        
        
        lista.append(tupla_actual)
            
    archivo.close()
    
  
    return lista