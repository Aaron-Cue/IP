########### GUIA 10 ############

### ARCHIVOS ###
# EJERCICIO 1.1

def contarLineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    lineas = 0
    
    for i in range(len(contenido)):
        if contenido[i] == '\n':
            lineas += 1
    lineas += 1
    archivo.close()
    
    return lineas


## EJERCICIO 1.2

def existePalabra(palabra: str, nombre_archivo: str) -> bool:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()

    return palabra in contenido


## EJERCICIO 1.3

def cantidadApariciones(nombre_archivo: str, palabra: str) -> int:
    archivo = open(nombre_archivo, 'r')
    lineas = archivo.readlines()
    apariciones = 0
    for linea in lineas:
        apariciones += linea.count(palabra)

    return apariciones 



## EJERCICIO 2

def clonarSinComments(name_file: str):
    archivo = open(name_file, 'r')

    lineas = archivo.readlines()
    lineas_sin_comments = []
    for linea in lineas:
        if sacarEspacios(linea)[0] != '#':
            lineas_sin_comments.append(linea)
    
    archivo.close()
    
    return ' '.join(lineas_sin_comments)

    

def sacarEspacios(linea: str) -> str:
    linea_sin_espacios = ""
    for caracter in linea:
        if caracter != ' ':
            linea_sin_espacios += caracter
    return linea_sin_espacios


## EJERCICIO 3

def lineasAlReverso(nombre_archivo: str):
    archivo = open(nombre_archivo, 'r')
    exLista = archivo.readlines()
    nuevo_archivo = []
    for i in range(len(exLista) -1 , -1, -1):
         nuevo_archivo.append(exLista[i])

    with open('reverso.txt', 'w') as reverso:
        reverso.writelines(nuevo_archivo)
    

## EJERCICIO 4 creando una copia
def agregarFrase(nombre_archivo:str, frase: str):
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.readlines()
    if '\n' in frase:
        frase_separada = frase.split('\n')
        contenido += frase_separada
    else:
        contenido.append(frase)

    return contenido

# EJERCICIO 4 modificando archivo original
def agregarFrasev2(nombre_archivo: str, frase: str):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write('\n' + frase)

    return None



## EJERCICIO 5
def agregarFraseComienzo(nombre_archivo: str, frase: str):
    with open(nombre_archivo, 'r+') as archivo:
        contenido_actual = archivo.read()
        archivo.seek(0)
        archivo.write(frase + '\n' + contenido_actual)

    return None


def agregarFraseComienzov2(nombre_archivo:str, frase: str):
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.readlines()
    if '\n' in frase:
        frase_separada = frase.split('\n')
        nuevo_contenido = frase_separada + contenido
        nuevo_contenido + contenido
    else:
        nuevo_contenido = [frase + '\n'] + contenido
        
    return nuevo_contenido


## EJERCICIO 6 lee en binario y devuelve una lista de palabras legibles

def leer_palabras_legibles(nombre_archivo):
    palabras_legibles = []
    
    with open(nombre_archivo, 'rb') as archivo:
        contenido_binario = archivo.read()
        contenido_texto = contenido_binario.decode('utf-8')
        
        palabra_actual = ""
        palabra_en_curso = False
        
        for caracter in contenido_texto:
            if caracter.isalnum() or caracter in [' ', '_']:
                palabra_actual += caracter
                palabra_en_curso = True
            else:
                if palabra_en_curso and len(palabra_actual) >= 5:
                    palabras_legibles.append(palabra_actual)
                palabra_actual = ""
                palabra_en_curso = False
        
        # Verificar la última palabra
        if palabra_en_curso and len(palabra_actual) >= 5:
            palabras_legibles.append(palabra_actual)
    
    return palabras_legibles


## EJERCICIO 7

def promedioEstudiante(lu):
    total_notas = 0
    cantidad_notas = 0
    archivo = open('notas.txt', 'r')
    for linea in archivo.readlines():
        datos = linea.split()
        if len(datos) == 4 and datos[0] == lu:
            nota = float(datos[3])
            total_notas += nota
            cantidad_notas += 1

    if cantidad_notas == 0:
        return 0

    promedio = total_notas / cantidad_notas
    return promedio
