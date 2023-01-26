
print ("Ingrese número:")

numingresado = int (input ())

fact = 1
for i in range (1, numingresado+1):
        fact*=i

if numingresado <= 0:
  print ("No se pueden sacar factoriales de números negativos")
else: 
  print (" El factorial de", numingresado, "es: ", fact) 

