"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""



def pregunta_01():
    
    nombre_del_archivo = "files/input/data.csv"
    suma_de_numeros = 0 
    
    
    archivo = open(nombre_del_archivo, "r") 

    
    for lineas_archivo in archivo:
        
   
        linea_limpia = lineas_archivo.strip()
        
    
       
            

        columnas = linea_limpia.split('\t')
        
        
        segunda_columna = columnas[1]
        
        numero_convertido = int(segunda_columna)
        
        suma_de_numeros = suma_de_numeros + numero_convertido
    
    # Paso 3: Cerrar el archivo cuando termines de usarlo
    archivo.close()
      
    return suma_de_numeros