###### GUIA 7 ###### 
import math

# EJERCICIO 1.1
def raizDe2() -> float:
    raiz: float = math.sqrt(2)
    raiz_redondeada: float = round(raiz, 4)
    return raiz_redondeada


#EJERCICIO 1.2
def imprimir_hola() -> str:
    print("hola") 


#EJERCICIO 1.3
def imprimir_un_verso() -> str:
    print("""te lo di todo,
toa la noche yo te pienso cuando tomo
ando mezclando la pastilla con el romo
y a tus exnovio yo le ofrezco plomo""")


#EJERCICIO 1.4
#funcion auxiliar factorial
def factorial(x: int) -> int:
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
        

def factorial_2() -> int:
    return factorial(2)


#EJERCICIO 1.5
def factorial_3() -> int:
    return factorial(3)


#EJERCICIO 1.6
def factorial_4() -> int:
    return factorial(4)


#EJERCICIO 1.7
def factorial_5() -> int:
    return factorial(5)


#EJERCICIO 2.1
def imprimir_saludo(s: str) -> str:
    print("hola", s)


#EJERCICIO 2.2
def raiz_cuadrada_de(x):
    return math.sqrt(x)


#EJERCICIO 2.3
def imprimir_dos_veces(estribillo: str) -> str:
    print(estribillo*2)
    
#EJERCICIO 2.4
def es_multiplo_de(x: int, y: int) -> bool:
    return x % y == 0
    

#EJERCICIO 2.5
def es_par(x: int) -> bool:
    return es_multiplo_de(x, 2)

#EJERCICIO 2.6
def cantidad_de_pizzas(comensales: int, cant_min_porciones: int) -> int:
    return math.ceil((comensales*cant_min_porciones+1)/8)
    

#EJERCICIO 3 resolver si if solos con and or not

#EJERCICIO 3.1
def alguno_es_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 or numero2 == 0

#EJERCICIO 3.2
def ambos_son_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 and numero2 == 0


#EJERCICIO 3.3
def es_nombre_largo(nombre: str) -> bool:
    return 3 <= len(nombre) <= 8

#EJERCICIO 3.4
def es_bisiesto(year: int) -> bool:
    return es_multiplo_de(year, 400)


#EJERCICIO 4

def peso_pino(altura: int) -> int:
    centimetros: int = altura*100
    exceso: int = centimetros - 300
    if centimetros <= 300:
        return centimetros * 3
    else:
        return 2 * exceso + 900

def es_peso_util(peso: int) -> bool:
    return 400 <= peso <= 1000 

def sirve_pino(altura: int) -> bool:
    return es_peso_util(peso_pino(altura))


#EJERCICIO 5 usando if else

#EJERCICIO 5.1

def devolver_el_doble_si_es_par(num: int) -> int:
    if num % 2 == 0:
        return 2*num
    else:
        return num

#EJERCICIO 5.2

def devolver_valor_si_es_par_sino_el_que_sigue(num: int) -> int:
    if num % 2 == 0: 
        return num
    else:
        return num + 1

#EJERCICIO 5.3

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(num: int) -> int:
    if es_multiplo_de(num, 3):
        return num * 2
    elif es_multiplo_de(num, 9):
        return num * 3
    else:
        return num
    
#EJERCICIO 5.4

def frase_segun_nombre(name: str) -> str:
    if len(name) >= 5:
        return "tu nombre tiene muchas letras!"
    else:
        "tu nombre tiene menos de 5 caracteres"
        
#EJERCICIO 5.5

def vacaciones_o_trabajar(genero: str, edad: int) -> str:
    if edad < 18 or (genero == "masculino" and edad >= 65) or (genero == "femenino" and edad >= 60):
        return "Anda de vacaciones"
    else: 
        return "Te toca trabajar"



#EJERCICIO 6 usar while

#EJERCICIO 6.1

def del1_al10() -> str:
    num = 1
    while num <= 10:
        print(num) 
        num += 1
        
#EJERCICIO 6.2 pares entre 10 y 40

def pares_entre_10_y_40() -> str:
    num = 10
    while num <= 40:
        if num % 2 == 0:
            print(num)
            num += 1
        else: 
            num += 1

# 0tra manera
def pares_entre_10_y_40_v2() -> str:
    num = 10
    while num <= 40:
        print(num)
        num += 2
        

#EJERCICIO 6.3

def eco_10_veces() -> str:
    i = 1
    while i <= 10:
        print("eco")
        i += 1
        
#EJERCICIO 6.4

def cuenta_regresiva(num: int) -> str:
    while num > 0:
        print(num)
        num -= 1
    print("despegue!")


#EJERCICIO 6.5

def viaje_en_el_tiempo(year_partida: int, year_llegada: int) -> str:
    year = year_partida - 1
    while year >= year_llegada:
        print(f"Viajo un year al pasado, estamos en el year {year}")
        year -= 1


#EJERCICIO 6.6

def viaje_en_el_tiempo_v2(year_partida: int) -> str:
    year = year_partida - 20
    while year >= -384:
        print(f"Viajo 20 years al pasado, estamos en el year {year}")
        year -= 20



#EJERCICIO 7

#EJERCICIO 7.1

def del1_al10_v2() -> str:
    for num in range(10):
        print(num)
       
#EJERCICIO 7.2 

def pares_entre_10_y_40_for() -> str:
    for num in range(10, 41):
        if num % 2 == 0:
            print(num)
        else:
            num += 1


# #EJERCICIO 7.3

def eco_10_veces_v2() -> str:
    for palabra in range(10):
        print("eco")
        palabra += 1


def eco_10_veces_v3() -> str:
    for palabra in range(10):
        palabra = "eco"
        print(palabra) 


# #EJERCICIO 7.4

def cuenta_regresiva(num: int) -> str:
    for numero in range(num, 0, -1):
        print(str(numero))
    return "despegue!"
        

# #EJERCICIO 7.5

def viaje_en_el_tiempo_for(year_partida: int, year_llegada: int) -> str:
    for year in range(year_partida - 1, year_llegada - 1, -1):
        print(f"Viajo en el tiempo, estamos en el year {year}")


# #EJERCICIO 7.6

def viaje_en_el_tiempo_for_v2(year_partida: int) -> str:
    for year in range(year_partida - 20, -384, -20):
        print(f"Viajo en el tiempo, estamos en el year {year}")
        

#EJERCICIO 9

def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g


print("respuesta 1")
print(ro(1))
print(ro(1))
print(ro(1))


print("respuesta 2")
print(rt(1, 0))
print(rt(1, 0))
print(rt(1, 0))




















