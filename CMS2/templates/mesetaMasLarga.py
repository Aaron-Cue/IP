from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

  
def todosIguales(l: List[int], i: int, j: int) -> bool:
  numero: int = l[i]
  for posicion in range(i, j+1):
    if l[posicion] != numero:
      return False
  return True
  

def hayMesetaDeLong(l: List[int], n: int) -> bool:
    if len(l) == 0:
        return n == 0

    if len(l) < n:
        return False

    i: int = 0
    j: int = n - 1

    while j < len(l):
        if todosIguales(l, i, j):
            return True
        i += 1
        j += 1

    return False 
  
  
def mesetaMasLarga(l: List[int]) -> int:  # [] -> 0
  
  if len(l) == 0:
    return 0
  
  i: int = len(l)
  
  while i >= 0:
    if hayMesetaDeLong(l, i):
      return i
    i -= 1
  
  return 1


if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))