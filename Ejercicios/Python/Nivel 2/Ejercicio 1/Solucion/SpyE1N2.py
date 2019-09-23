A=35
B=20
valor = []
valin = str(raw_input("\nIngrese variables (separadas por comas): "))
elems=[x for x in valin.split(',')]
for d in elems:
        valor.append(str(int(round((2*A*B)/round(float(d))))))
print ("Numeros calculados: " + ','.join(valor))
