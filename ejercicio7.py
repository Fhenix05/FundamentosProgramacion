'''
Ejercicio 7:
  Programa que transforme los minutos en horas y minutos
Entradas:
  minutos: int
Salidas:
  horas: int
  minutos: int
'''

minutos = input("Ingresa los minutos: ")
minutos = int(minutos)
h = minutos // 60
min = minutos % 60
print("Las horas son: ",h , ":", min)