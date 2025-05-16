"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """


    nombre_del_archivo = "files/input/data.csv"
    
    
    conteo = {}
  
    archivo = open(nombre_del_archivo, "r")


    for lineas_archivos in archivo:
        linea_limpia = lineas_archivos.strip()
        
            
        columnas = linea_limpia.split('\t')

        fecha_completa = columnas[2] 
        
        mes = fecha_completa[5:7]
        
        conteo[mes] = conteo.get(mes, 0) + 1
            
    archivo.close()
    
    lista_de_tuplas = list(conteo.items())
    
    resultado_ordenado = sorted(lista_de_tuplas)
      
    return resultado_ordenado
