import math
y1 = input("\nIngrese moviento hacia arriba: ")
y2 = input("Ingrese moviento hacia abajo: ")
x1 = input("Ingrese moviento hacia la izquierda: ")
x2 = input("Ingrese moviento hacia la derecha: ")
desy = abs(y1-y2)
desx = abs(x1-x2)
print ("\n\n El dron se desplazo " + str(int(round(math.sqrt(desy**2+desx**2)))) + " unidades.\n")
