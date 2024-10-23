"""
Programa que calcule la calificacion final de un alumno 
Entradas:
  calificacion A
  calificacion B
  calificacion C
  cal.examen
  cal.trabajo final
salidas:
  calificacion final
"""

cal1 = input("Ingresa tu calificacion del primer parcial: ")
cal1 = int(cal1)
cal2 = input("Ingresa tu calificacion del segundo parcial: ")
cal2 = int(cal2)
cal3 = input("Ingresa tu calificacion del tercer parcial: ")
cal3 = int (cal3)
calexam = input("Ingresa tu calificacion del examen: ")
calexam = int(calexam)
caltf = input("Ingresa tu calificacion del trabajo final: ")
caltf = int(caltf)
promedio = (cal1 + cal2+ cal3)/3
cf = ((promedio * 55)/100) + ((calexam * 30)/100) + ((caltf*15)/100)
print ("tu calificacion final es: ", cf)