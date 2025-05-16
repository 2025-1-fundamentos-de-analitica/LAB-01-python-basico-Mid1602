"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

 """
   
    nombre_del_archivo = "files/input/data.csv"
    
    min_valores = {} 
    max_valores = {} 
    

    archivo = open(nombre_del_archivo, "r")
    
    for linea in archivo:
        linea_limpia = linea.strip().split('\t')
        
        letra = linea_limpia[0]
        valor = int(linea_limpia[1]) 

        if letra not in min_valores:
            min_valores[letra] = valor
            max_valores[letra] = valor
        else:
            if valor < min_valores[letra]:
                min_valores[letra] = valor
            
            if valor > max_valores[letra]:
                max_valores[letra] = valor
            
    archivo.close()
    
    lista_sin_ordenar = []
    for letra_k in max_valores: 
        tupla = (letra_k, max_valores[letra_k], min_valores[letra_k])
        lista_sin_ordenar.append(tupla)
        
    resultado_ordenado = sorted(lista_sin_ordenar)
      
    return resultado_ordenado

