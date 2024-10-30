"""
Calcula y muestra la distancia de dos pares de numeros x1, y1, x2, y2.
  Entredas:
   coordenada: x1 y1
   coordenada: x2 y2 
  Salidas:
    distancia  
"""

coordenadax = input("Escribe la coordenada x: ")
coordenadax = int(coordenadax)
coordenaday = input("Escribe la coordenada y: ")
coordenaday = int(coordenaday)
coorx = input("Escribe la coordenada x2: ")
coorx = int(coorx)
coory = input("Escribe la coordenada y2: ")
coory = int(coory)
d = ((coorx - coordenadax)**2 + (coory - coordenaday)**2)**0.5
print("La distancia es: ", d)