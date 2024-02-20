from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int:
    if hayRuta(vuelos, origen, destino):
        for cant in range(1, 100):
            if largoDeRuta(obtenerRuta(vuelos, origen, destino), origen, destino, cant):
                return cant
        return "no se encontro cantidad"
    else:
        return -1
    

def soloParteUnVueloDeCadaCiudad(vuelos: List[Tuple[str, str]]) -> bool:

    if len(vuelos) == 1:
        return True

    for i in range(len(vuelos)):
        j = i + 1
        while j < len(vuelos):
            if vuelos[j][0] == vuelos[i][0]:
                return False
            j += 1

    return True


def soloLlegaUnVueloACadaCiudad(vuelos: List[Tuple[str, str]]) -> bool:
    # True si cada segundo elemento de las tuplas son distintos
    if len(vuelos) == 1:
        return True

    for i in range(len(vuelos)):
        j = i + 1
        while j < len(vuelos):
            if vuelos[j][1] == vuelos[i][1]:
                return False
            j += 1

    return True


def sinRepetidos(ruta: List[Tuple[str, str]]) -> bool:
    
    if len(ruta) <= 1:
        return True
    
    for i in range(len(ruta)):
        j = i + 1
        while j < len(ruta):
            if ruta[i] == ruta[j]:
                return False
            j += 1

    return True


def vuelosValidos(ruta: List[Tuple[str, str]], vuelos: List[Tuple[str, str]]) -> bool:

    if sinRepetidos(ruta):
        for i in range(len(ruta)):
            if not (ruta[i] in vuelos):
                return False
        
        return True
    
    
def caminoDeVuelos(ruta: List[Tuple[str, str]]) -> bool:
    
    for i in range(1, len(ruta), 1):
        if ruta[i][0] != ruta[i-1][1]:
            return False
    
    return True


def largoDeRuta(ruta: List[Tuple[str, str]], origen: str, destino: str, longCamino: int) -> bool:
    
    if not (sinRepetidos(ruta)):
        return False
    
    if len(ruta) == 0:
        return False
    
    if len(ruta) == 1 and ruta[0][0] == origen and ruta[0][1] == destino and len(ruta) == longCamino:
        return True
    
    if ruta[0][0] == origen and ruta[len(ruta)-1][1] == destino and len(ruta) == longCamino:
        return True
    else:
        return False


def hayRuta(vuelos: List[Tuple[str, str]], origen: str, destino: str) -> bool:
    # True si existe una ruta con vuelos válidos, al menos un vuelo que parta desde origen y termine en destino en secuencia
    
    for vuelo in vuelos:
        if vuelo == (origen, destino):
            return True                   # Verifica si hay un vuelo directo
    
    hayOrigen = False
    hayDestino = False
    ruta = []
    
    for vuelo in vuelos:
        if vuelo[0] == origen:
            hayOrigen = True         # Verificar si hay un vuelo que parta desde origen
            ruta.append(vuelo)       # Hace que la ruta empiece con un vuelo desde el origen       
        elif vuelo[1] == destino:
            hayDestino = True        # Verificar si hay un vuelo que llegue a destino
        
    if hayOrigen and hayDestino:
        # Si se encontró un vuelo que parte desde origen y un vuelo que llega a destino, buscar una secuencia que conecte la ruta
        while ruta[-1][1] != destino:
            encontrado = False
            for vuelo in vuelos:
                if vuelo[0] == ruta[-1][1] and vuelo[1] not in [r[1] for r in ruta]:
                    ruta.append(vuelo)
                    encontrado = True
                    break
            if not encontrado:
                break
        
        if ruta[-1][1] == destino:
            # Si el último vuelo en la ruta llega a destino, se ha encontrado una ruta válida
            return True
    
    return False

    
def obtenerRuta(vuelos: List[Tuple[str, str]], origen: str, destino: str) -> List[Tuple[str, str]]:
    # Verifica si hay un vuelo directo desde origen a destino
    for vuelo in vuelos:
        if vuelo == (origen, destino):
            return [(origen, destino)]
    
    # Verifica si hay una secuencia de vuelos que conecte origen y destino
    ruta = [origen]  # Inicializa la ruta con el origen
    visitados = set()  # Conjunto de ciudades visitadas
    
    while ruta[-1] != destino:
        ciudad_actual = ruta[-1]
        encontrado = False
        
        for vuelo in vuelos:
            if vuelo[0] == ciudad_actual and vuelo[1] not in visitados:
                ruta.append(vuelo[1])
                visitados.add(vuelo[1])
                encontrado = True
                break
        
        if not encontrado:
            return []  # No se encontró una secuencia que conecte origen y destino
    
    ruta_vuelos = [(ruta[i], ruta[i+1]) for i in range(len(ruta)-1)]
    return ruta_vuelos



if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))