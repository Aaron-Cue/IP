from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"



def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:

  if pedidos.empty():
    return []
  
  pedidos_procesados = []
  
  
  for pedido in list(pedidos.queue):
  # a cada pedido se le agrega las claves de precio y estado segun el stock
    pedido["precio_total"] = precioSegunStock(pedido, stock_productos, precios_productos)
    pedido["estado"] = estadoSegunStock(pedido, stock_productos)
    pedidos_procesados.append(procesarPedido(pedido, stock_productos))    
    stock_productos = stockActualizado(pedido, stock_productos)
    
  return pedidos_procesados


def procesarPedido(pedido: Dict[str, Union[int, str, Dict]], stock_productos: Dict[str, int]) -> Dict[str, Union[int, str, Dict]]:
  # dado un pedido modifique las cantidades de productos segun el stock
  for producto, cantidad in pedido['productos'].items():
    if cantidad > stock_productos[producto]:
      pedido['productos'][producto] = stock_productos[producto]
      
  return pedido



def stockActualizado(pedido: Dict[str, Union[int, str, Dict]], stock_productos: Dict[str, int]) -> Dict[str, int]:
# recorre cada producto y cantidad, si hay suficiente stock resta la cantidad del pedido, de lo contrario lo actualiza a 0
  for producto, cantidad in pedido["productos"].items():
    if cantidad > stock_productos[producto]:
      stock_productos[producto] = 0
    else:
      stock_productos[producto] -= cantidad
      
  return stock_productos



def estadoSegunStock(pedido: Dict[str, Union[int, str, Dict]], stock_productos: Dict[str, int]) -> str:
  # recorre cada producto y cantidad, compara con el stock, si en algun caso falta stock devuelve incompleto sino completo
  for producto, cantidad in pedido["productos"].items():
    if cantidad > stock_productos[producto]:
      return "incompleto"
    
  return "completo"



def precioSegunStock(pedido: Dict[str, Union[int, str, Dict]],
                     stock_productos: Dict[str, int],
                     precios_productos: Dict[str, float]) -> float:
  # recorre cada producto y cantidad, suma la cantidad de cada producto si hay stock sino lo que haya de stock
  precio = 0
  for producto, cantidad in pedido["productos"].items():
    if stock_productos[producto] >= cantidad:          # si hay suficiente stock
      precio += cantidad*precios_productos[producto]
    else:                                              # si no hay suficiente stock
      precio += stock_productos[producto]*precios_productos[producto]
    
  return precio




if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))
