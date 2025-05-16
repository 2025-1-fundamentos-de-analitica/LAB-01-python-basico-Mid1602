"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
  
    
    nombre = "files/input/data.csv"
    archivo = open(nombre, "r")
    conteo_letras = {}


    for lineas_archivo in archivo:
        
        linea_limpia = lineas_archivo.strip()

        letra = linea_limpia.split('\t')[0]
        conteo_letras[letra] = conteo_letras.get(letra, 0) + 1
            

    archivo.close()
    return sorted(list(conteo_letras.items()))
    