"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    nombre_del_archivo = "files/input/data.csv"
    
    archivo = open(nombre_del_archivo, "r")
    
    letras_unicas_por_valor = {}
    
    
    for linea in archivo:
        
        linea_limpia = linea.strip().split('\t')
        
        
        letra = linea_limpia[0]
        valor = int(linea_limpia[1]) 
        
        if valor not in letras_unicas_por_valor:
            letras_unicas_por_valor[valor] = set() # Inicializar con un conjunto vacío
        
        # Si la letra ya está en el conjunto ---> .add() no hace nada (no duplica).
        letras_unicas_por_valor[valor].add(letra)
            
    archivo.close()
    
   
    lista = []
    
    for valor_num, letras_set in letras_unicas_por_valor.items():
       
        lista_letras_ordenadas = sorted(list(letras_set))
        
        tupla = (valor_num, lista_letras_ordenadas)
        lista.append(tupla)
    
    resultado_ordenado_final = sorted(lista)
      
    return resultado_ordenado_final

