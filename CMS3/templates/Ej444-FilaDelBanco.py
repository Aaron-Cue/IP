from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"


def avanzarFila(fila: Queue, min: int):
  
    # minutos de atencion
    caja1_tiempo_atencion = 10  
    caja2_tiempo_atencion = 4  
    caja3_tiempo_atencion = 4   
    caja3_tiempo_volver = 3     

    # minutos de apertura
    tiempo_actual = 0
    tiempo_problema = 0  
    caja1_abre = 1
    caja2_abre = 3
    caja3_abre = 2

    # agrego persona a la fila
    if fila.empty():
      fila.put(1)
    else:
      ultima_persona = fila.queue[-1]
      fila.put(ultima_persona + 1)
  
    
    while tiempo_actual <= min:
      
      if tiempo_actual == tiempo_problema + 3:
        fila.put(tiempo_problema)
      
      
      if tiempo_actual != 0 and tiempo_actual % 4 == 0:
        ultima_persona = fila.queue[-1]
        fila.put(ultima_persona + 1)
      
      
      if tiempo_actual >= caja1_abre:
          if not fila.empty():
              fila.get()
              caja1_abre += caja1_tiempo_atencion

      if tiempo_actual >= caja2_abre:
          if not fila.empty():
              fila.get()
              caja2_abre += caja2_tiempo_atencion

      if tiempo_actual >= caja3_abre:
          if not fila.empty():
            cliente_problema = fila.get()
            caja3_abre += caja3_tiempo_atencion
            tiempo_problema = tiempo_actual
# cliente_problema debe volver a la fila en 3 minutos        

      tiempo_actual += 1

    return list(fila.queue)

fila1 = Queue()
fila1.put(1)
fila1.put(2)
fila1.put(3)
minuto0 = 0
minuto1 = 1
minuto2 = 2
minuto3 = 3
minuto4 = 4
minuto5 = 5
print(avanzarFila(fila1, minuto0))
print(avanzarFila(fila1, minuto1))
print(avanzarFila(fila1, minuto2))
print(avanzarFila(fila1, minuto3))
print(avanzarFila(fila1, minuto4))


# recibe una fila puede ser: [] , [1], [1,2,3] , [1,2,...,n]
# el banco abre a las 10:00, al abrir una persona se incorpora a la fila, luego una cada 4 minutos
# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero esa persona vuelve a la fila pasados 3 minutos
# si hay mas de una caja disponible, la prioridad es caja1 luego caja2 luego caja3






















if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)