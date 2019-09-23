lista=[]
for x in range(2000, 4000):
    if (x%7==0) and (x%5!=0):
        lista.append(str(x))
print (','.join(lista))
