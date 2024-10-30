"""
Programa que dado un número de dos cifras que permita obtener el número invertido
  Entradas:
    número
  Salidas:
    número invertido 
"""

num = input("Ingresa un número de dos digitos: ")
num = int(num)
dec = num//10
uni = num % 10
ninv = (uni * 10) + dec
print ("El número invertido es: ",ninv)