'''
Ejercicio 4:
  Programa que calcule la suma, resta, multiplicacion y division de dos numeros  
Entradas:
  numeroA: int
  numeroB: int
Salidas:
  suma: intenger
  resta: interger
  multiplicacion: interger
  division: interger
'''
numeroa = input("Ingresa el numero: ")
numeroa = int(numeroa)
numerob = input("Ingresa el numero: ")
numerob = int(numerob)
suma = numeroa + numerob
resta = numeroa - numerob
multiplicacion = numeroa * numerob
division = numeroa / numerob
print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicacion es: ",multiplicacion)
print("La division es: ",division)