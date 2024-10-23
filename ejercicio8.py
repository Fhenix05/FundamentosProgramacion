'''
Ejercicio 8:
  Programa que calcule el dinero de un sueldo base mas un 10% extra por concepto de comision de tres ventas que realizo en el mes tomando en cuenta su sueldo base y comisiones 
Entradas:
  Sueldo: int
  Variable 1: int
  Variable 2: int
  Variable 3: int
Salidas:
  Dinero en un mes
'''

variable1 = input("Ingresar venta: ")
variable1 = int(variable1)
variable2 = input("ingresar venta: ")
variable2 = int(variable2)
variable3 = input("ingresar venta ")
variable3 = int(variable3)
sueldo = input("Ingresar sueldo ")
sueldo = int(sueldo)
v1 = (variable1*10)/100
v2 = (variable2*10)/100
v3 = (variable3*10)/100
dinero = (sueldo + v1 + v2 + v3)
print("Tu sueldo es", dinero , "pesos")