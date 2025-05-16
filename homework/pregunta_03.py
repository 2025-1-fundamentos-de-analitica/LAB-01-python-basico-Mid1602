"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    nombre_del_archivo = "files/input/data.csv" 
    

    sumas_por_letra = {}
    

    archivo = open(nombre_del_archivo, "r")


    for lineas_archivos in archivo:
       
        linea_limpia = lineas_archivos.strip()
   
            

        columnas = linea_limpia.split('\t')
        
        
        letra = columnas[0]
        
 
        valor_texto = columnas[1]
        
        
        valor_numerico = int(valor_texto)
        
        
        sumas_por_letra[letra] = sumas_por_letra.get(letra, 0) + valor_numerico
            
   
    archivo.close()
    

    lista_de_tuplas = list(sumas_por_letra.items())
    
   
    resultado_ordenado = sorted(lista_de_tuplas)
      
    return resultado_ordenado