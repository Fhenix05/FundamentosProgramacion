"""
Programa que lea un número y muestre su raíz cuadrada y su raíz cubica
  Entradas:
    número
  Salidas:
    raíz cuadrada 
    raíz cubica 
"""

num = input("Ingresa un número: ")
num = int(num)
rcua = (num**0.5)
rcub = (num**0.33)
print ("La raíz vubica es: ", rcua)
print ("La raíz cubica es: ", rcub)