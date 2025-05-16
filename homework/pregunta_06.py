"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    nombre_del_archivo = "files/input/data.csv"
    
    min_valores = {} 
    max_valores = {} 
    
    archivo = open(nombre_del_archivo, "r")
    
    for linea in archivo:
        
        linea_limpia = linea.strip()
        
    

        partes_linea = linea_limpia.split('\t')
        
   
        columna = partes_linea[4] 
        
        #  (están separados por ',')
        pares_individuales = columna.split(',') # ['jjj:12', 'bbb:3', ...]
        
        for par in pares_individuales:
            # par es algo como "jjj:12"
            
   
            partes_del_par = par.split(':') # Ejemplo: ['jjj', '12']
            
            clave_tres_letras = partes_del_par[0] 
            valor_asociado = int(partes_del_par[1]) 
            
         
            if clave_tres_letras not in min_valores:
                
                min_valores[clave_tres_letras] = valor_asociado
                max_valores[clave_tres_letras] = valor_asociado
            else:
                
                if valor_asociado < min_valores[clave_tres_letras]:
                    min_valores[clave_tres_letras] = valor_asociado
                
                if valor_asociado > max_valores[clave_tres_letras]:
                    max_valores[clave_tres_letras] = valor_asociado
            
    archivo.close()
    
    lista_sin_ordenar = []
    for clave_k in min_valores: 
        tupla = (clave_k, min_valores[clave_k], max_valores[clave_k]) 
        lista_sin_ordenar.append(tupla)
        
    resultado_ordenado = sorted(lista_sin_ordenar)
      
    return resultado_ordenado

