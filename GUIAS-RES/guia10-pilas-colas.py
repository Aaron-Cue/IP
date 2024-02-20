########### GUIA 10 ############
import random
from queue import LifoQueue
from queue import Queue

### PILAS ###
# EJERCICIO 8 generar n enteros desde hasta inclusivos
def generarNrosAlAzar(n: int, desde: int, hasta: int) -> list[int]:
    numeros = list(range(desde, hasta + 1, 1))
    return random.sample(numeros, n)


# EJERCICIO 9 
def numeroAzarConPila(n: int, desde:int, hasta: int):
    numeros = list(range(desde, hasta + 1, 1))
    pila = LifoQueue()
    while n > 0:
        numRandom = random.sample(numeros, 1)
        pila.put(numRandom[0])
        n -= 1
    
    # pasar los elementos de la pila a una lista para verificar que funcione
    elementos_pila = []
    while not pila.empty():
        elementos_pila.append(pila.get())
    
    return elementos_pila


# EJERCICIO 10 dada una pila, cuente la cantidad de elementos que contiene.
def cantidadElementos(p):
    elementos = 0
    while not p.empty():
        elementos += 1
        p.get()
        
    return elementos


# EJERCICIO 11 
def buscarElMaximo(p):
    if p.empty():
        return "lista sin elementos"

    # agregar un elemento a una variable, recorrer cada elemento de la pila y compararloo con la variable , de ser mayor reemplazarla, devolver la variable
    maximo = p.get()
    while not p.empty():
        elemento = p.get()
        if elemento > maximo:
            maximo = elemento
    
    return maximo
        

# EJERCICIO 12 utilizando una sola pila
def estaBienBalanceada(formula: str) -> bool:
    pila = LifoQueue()

    for elemento in formula:
        if elemento == "(":
            pila.put(elemento)
        elif elemento == ")":
            if pila.empty() or pila.get() != "(":
                return False

    return pila.empty()



### COLAS ###
# EJERCICIO 13 generarnrosalazasr devuelve una lista
def colaDeNumerosAlAzar(n: int, desde: int, hasta: int) -> Queue:
    cola = Queue()
    while n > 0:
        numeroRandom = generarNrosAlAzar(1, desde, hasta)
        cola.put(numeroRandom[0])
        n -= 1
        
    return cola


## EJERCICIO 14
def cantidadElementos(cola) -> int:
    elementos = 0
    while not cola.empty():
        cola.get()
        elementos += 1
    return elementos
   
        
## EJERCICIO 15
def buscarElMaximo(cola) -> int:
    maximo = cola.get()
    while not cola.empty():
        elemento = cola.get()
        if elemento > maximo:
            maximo = elemento
    
    return maximo


## EJERCICIO 16.1 genere una cola de los numeros del 0 al 99 ordenados al azar
def armarSecuencuaDeBingo() -> Queue[int]:
    numeros = list(range(0, 100))
    random.shuffle(numeros)

    bolillero = Queue()
    i = 0
    while i < 100:
        bolillero.put(numeros[i])
        i += 1
        
    return bolillero   
    

## EJERCICIO 16.2 devuelve la cantidad de jugadas necesarias para completar el carton
def jugarCartonDeBingo(carton: list[int], bolillero: Queue[int]) -> int:
    jugadas = 0
    while len(carton) > 0:
        numero = bolillero.get()
        if numero in carton:
            carton.remove(numero)
        jugadas += 1
    
    return jugadas


## EJERCICIO 17 recibe una cola de paciente, cada uno con su grado de urgencia del 1 al 10, su nombre y su especialidad. debe devolver la cantidad de pacientes con grado de urgencia, se considera urgente si es grado 1 o grado 2 o grado 3

def nPacientesUrgentes(cola: Queue[tuple[int, str, str]]) -> int:
    
    pacientes_urgentes = 0
    urgencia = [1, 2, 3]
    
    while not cola.empty():
        paciente = cola.get()
        if paciente[0] in urgencia:
            pacientes_urgentes += 1
        
    return pacientes_urgentes
        

### DICCIONARIOS ###

## EJERCICIO 18 lee el archivo, y agrupar en un diccionario la cantidad de palabras de acuerdo a su longitud
def agruparPorLongitud(nombre_archivo: str) -> dict:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read() 
    palabras = contenido.split()  # lista con cada palabra del archivo
    
    diccionario = {}
    
    for palabra in palabras:
        longitud = len(palabra)
        if longitud in diccionario:
            diccionario[longitud] += 1
        else:
            diccionario[longitud] = 1

    return diccionario


## EJERCICIO 20 devuelve la palabra que mas veces aparece 
def agruparPorFrecuencia(nombre_archivo: str) -> str:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read() 
    palabras = contenido.split()  # lista con cada palabra del archivo
    
    diccionario = {}
    
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    clave_mayor = None
    valor_mayor = float('-inf')
    
    for clave, valor in diccionario.items():
        if valor > valor_mayor:
            clave_mayor = clave
            valor_mayor = valor
    
    return clave_mayor 

print(agruparPorFrecuencia('prueba.txt'))

