"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}
    """
    nombre_del_archivo = "files/input/data.csv"

    conteo = {}
    
    archivo = open(nombre_del_archivo, "r")
    
    for linea in archivo:
        linea_limpia = linea.strip().split('\t')
        
            
        
        
        columna = linea_limpia[4] #  "jjj:12,bbb:3,ddd:9"
        
        pares_individuales = columna.split(',') #  ['jjj:12', 'bbb:3', ...]
        
        for par in pares_individuales:
    
            partes_del_par = par.split(':') #  ['jjj', '12']
            
            clave_tres_letras = partes_del_par[0] #  'jjj'
     
            conteo[clave_tres_letras] = conteo.get(clave_tres_letras, 0) + 1
            
         
    archivo.close()
    
    
    items_ordenados = sorted(list(conteo.items()))
    
    diccionario = {}
    for clave, valor in items_ordenados:
        diccionario[clave] = valor
        
    return diccionario
