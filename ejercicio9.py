"""
Programa que calcule el descuento del 15% sobre el total de la compra
Entradas:
  precio
Salidas:
  descuento
"""
 
precio=input("Ingresa el precio del producto: ")
precio=int(precio)
descuento=(precio*15)/100
total=(precio - descuento)
print("El precio es: ", total)