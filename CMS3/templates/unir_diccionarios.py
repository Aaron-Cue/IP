from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,str]]) -> Dict[str,List[str]]:
# toma una lista de diccionarios y devuelve la union de todos ellos en otro diccionario
  if len(a_unir) == 0:
    return {}
  elif len(a_unir) == 1:
    return a_unir[0]
  
  diccionario = {}
  for dicc in a_unir:
    for key, value in dicc.items():
            if key in diccionario:
                diccionario[key].append(value)
            else:
                diccionario[key] = [value]

  return diccionario



if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))