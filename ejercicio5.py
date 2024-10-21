'''
Ejercicio 5:
  Programa que transforme los grados Farenheit a grados celsius 
Entradas:
  grados Farenheit: int
Salidas:
  grados Celsius
'''
gradosF = input("Ingresa el grado F: ")
gradosF = int(gradosF)
gradosC = (gradosF-32)/1.8
print("El grados Celsius es: ",gradosC)