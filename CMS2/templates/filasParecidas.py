from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
  
  
#pred filaAnteriorMasN
def filaAnteriorMasN(matriz: List[List[int]], i, n: int) -> bool: #mal-> probar i: int

  indice = 0
  
  for numero in matriz[i]:
    if numero != matriz[i-1][indice] + n:
      return False
    indice += 1
  
  return True
     
     
#pred filasParecidasAanterior
def filasParecidasAanterior(matriz: List[List[int]], n: int) -> bool:
# 1 <= i <= len(matriz)-1  osea para cada sublista -> filaAnteriorMaN(m, i, n)
  for i in range(1, len(matriz)):
    if filaAnteriorMasN(matriz, i, n) == False:
      return False
  
  return True


def filasParecidas(matriz: List[List[int]]) -> bool : 
#recibe una matriz donde cada sublista debe tener la misma longitud
  for n in range(1, 100):
    if filasParecidasAanterior(matriz, n):
      return True
  
  return False   



if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))