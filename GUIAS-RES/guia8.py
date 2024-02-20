##### GUIA 8 #####

import random

#EJERCICIO 1.1

#usando in
def pertenece(s: list, n: int) -> bool:
    return n in s 

#usando bucle for
def pertenece_v2(s: list, n: int) -> bool:
    for numero in s:  
        if numero == n:
            return True
    return False
    
#usando count
def pertenece_v3(s: list, n: int) -> bool:
    return s.count(n) > 0



#JERCICIO 1.2

#usando for
def divideATodos(s: list, n: int) -> bool: #con n != 0
    for numero in s:
        if numero % n != 0:
            return False
    return True
           
#usando all
def divideATodos_v2(s: list, n: int) -> bool: #con n != 0
    return all(numero % n == 0 for numero in s)


#EJERCICIO 1.3

def sumaTotal(s: list) -> int:
    sum = 0
    for numero in s:
        sum += numero
    return sum


#EJERCICIO 1.4

#usando for
def ordenados(s: list) -> bool:
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            return False
    return True


#usando sorted
def ordenados_v2(s: list) -> bool:
    return s == sorted(s)

#usando all
def ordenados_v3(s: list) -> bool:
    return all(s[i] <= s[i+1] for i in range(len(s) - 1))


#EJERCICIO 1.5

#usando for
def palabraLarga(s: list) -> bool:  # s una lista de palabras 
    for palabra in s:
        if len(palabra) > 7:
            return True
    return False
            
#usando any
def palabraLarga_v2(s: list) -> bool:
    return any(len(palabra) > 7 for palabra in s)         


#EJERCICIO 1.6


def esPalindroma(palabra: str) -> bool:
    return palabra == palabra[::-1]

# usando for
def esPalindroma_v2(palabra: str) -> bool:
    longitud = len(palabra)
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - i - 1]:
            return False
    return True


#EJERCICIO 1.7
def contrasena(password: str) -> str:
    tiene_minuscula = False
    tiene_mayuscula = False
    tiene_numero = False
    
    if len(password) <= 8:
        return "ROJA"
    
    for letra in password:
        if 96 < ord(letra) < 123:
            tiene_minuscula = True
        elif 64 < ord(letra) < 91:
            tiene_mayuscula = True
        elif 47 < ord(letra) < 58:
            tiene_numero = True
                
    if tiene_minuscula and tiene_mayuscula and tiene_numero:
        return "VERDE"
    else:
        return "AMARILLA"


#EJERCICIO 1.8

def saldo_actual(lt: list) -> int:
    saldo = 0
    
    for operacion in lt:
        if operacion[0] == "I":
            saldo += operacion[1]
        else:
            saldo -= operacion[1]
    
    return saldo


#EJERCICIO 1.9  #true si tiene al menos 3 vocales distintas

def tres_vocales_distintas(palabra: str) -> bool:
    letra_a = False
    letra_e = False
    letra_i = False
    letra_o = False
    letra_u = False
    cant_vocales = 0
    palabra_min = palabra.lower()
    
    for letra in palabra_min:
        if letra == "a":
            letra_a = True
        elif letra == "e":
            letra_e = True
        elif letra == "i":
            letra_i = True
        elif letra == "o":
            letra_o = True
        elif letra == "u":
            letra_u = True
    
    if letra_a:
        cant_vocales += 1
    
    if letra_e:
        cant_vocales += 1
        
    if letra_i:
        cant_vocales += 1
        
    if letra_o:
        cant_vocales += 1
        
    if letra_u:
        cant_vocales += 1
    
    
    if cant_vocales >= 3:
        return True
    else:
        return False


#o usando conjuntos

def tres_vocales_distintas_v2(palabra: str) -> bool:
    palabra_min = palabra.lower()
    vocales = set()

    for letra in palabra_min:
        if letra in "aeiou":
            vocales.add(letra)

            if len(vocales) >= 3:
                return True

    return False

    
    
#EJERCICIO 2.1

def remplazar_posiciones_pares(xs: list) -> list:
    for i in range(len(xs)):
        if i % 2 != 0:
            xs[i] = 0
    return xs

#EJERCICIO 2.2
#nose


#EJERCICIO 2.3 

def sacarVocales(texto: str) -> str:
    new_text = ""
    for letra in texto:
        if letra not in "aeiouAEIOU":
            new_text += letra
    return new_text



#EJERCICIO 2.4

def reemplazaVocales(text: str) -> str:
    for letra in text:
        if letra in "aeiouAEIOU":
            text = text.replace(letra, "_")
    return text


#EJERCICIO 2.5

def daVueltaStr(texto: str) -> str:
    textoReverso = ""
    for i in range(len(texto) - 1, -1 , -1):
        textoReverso += texto[i]
    return textoReverso


#EJERCICIO 3.1
     
def nombresAlumnos() -> list:
    listaAlumnos = []
    nombre = input("Nombre del alumno: ")
    
    if nombre != "listo":
        listaAlumnos.append(nombre)
        listaAlumnos.extend(nombresAlumnos())
    
    return listaAlumnos


#EJERCICIO 3.2

def historialMondedero() -> list:
    historial = []
    operacion = input("indique la operacion a realizar: ")
    if operacion == "C" or operacion == "D":
        monto = input("indique el monto: ")
        historial.append((operacion, monto))
        historial.extend(historialMondedero())
    return historial


#EJERCICIO 3.3
     
def juego_7yMedio():
    numero_aleatorio = random.randint(1, 12)
    while numero_aleatorio == 8 or numero_aleatorio == 9:
        numero_aleatorio = random.randint(1, 12)
    
    if numero_aleatorio >= 10:
        numero_aleatorio = 0.5
    
    puntaje = numero_aleatorio
    historial = [puntaje]
    decision = input(f"Su puntaje es de {puntaje}, ¿desea una carta o plantarse?: ")
    
    while decision.lower() == "carta":
        numero_aleatorio = random.randint(1, 12)
        while numero_aleatorio == 8 or numero_aleatorio == 9:
            numero_aleatorio = random.randint(1, 12)
        
        if numero_aleatorio >= 10:
            numero_aleatorio = 0.5
        
        puntaje += numero_aleatorio
        historial.append(numero_aleatorio)
        print(f"Su puntaje actual es de {puntaje}")
        
        if puntaje > 7.5:
            print("Te pasaste de 7.5. ¡perdiste!")
            break
        
        decision = input("¿Desea pedir otra carta o plantarse?: ")
        
    return f"su puntaje final es de {puntaje}, y su historial de cartas es {historial}"



#EJERCICIO 4.1

def perteneceACadaUno(xxs: list, e: int) -> list:
    resultados = []
    for lista in xxs:
        if pertenece(lista, e):
            resultados.append(True)
        else:
            resultados.append(False)
    return resultados
    

#EJERCICIO 4.2

def esMatriz(xxs: list) -> bool:
    longitud = len(xxs[0])
    for lista in xxs:
        if len(lista) != longitud:
            return False
    return True
            
            
#EJERCICIO 4.3

                  #recibe una matriz
def filasOrdenadas(xxs: list) -> list:  
    resultados = []
    for lista in xxs:
        if ordenados(lista):
            resultados.append(True)
        else:
            resultados.append(False)
        
    return resultados



#EJERCICIO 4.4


#que sea aleatoria
# a esa matriz elevarla a la p

def potenciaMatriz(d:int, p:float) -> list:
    matriz_aleatoria = [[random.randint(1, 1000) ** p for elem in range(d)] for i in range(d)] 
    return matriz_aleatoria
     
    

def pablo(palabra) -> str:
    minusc = palabra.lower()
    new =''
    for letra in minusc:
        if letra != 'a':
            new += letra
    print(new)
        
pablo('zarasas')
juego_7yMedio()