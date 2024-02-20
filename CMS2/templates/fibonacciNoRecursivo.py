import sys

def fibonacciNoRecursivo(n: int) -> int:
  if n == 0:
    return 0
  secuencia = [0, 1]
  for i in range(0, n-1):
    secuencia.append(secuencia[i] + secuencia[i+1])
  return secuencia[len(secuencia)-1]
  
  
if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))