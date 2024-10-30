"""
Programa que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
  Entradas:
    Numero A
    numero B
  Salidas:
    Numero C
    Numero B
"""

n1 = input("Escribe un número ")
n1 = int(n1)
n2 = input("Escribe un número ")
n2 = int(n2)
nA = n1
n1 = n2
n2 = nA
nf = "La variable final es ",n1, "y", n2
print (nf)