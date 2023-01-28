#Triángulo: Escriba un programa que reciba un número del usuario y
#despliegue en pantalla el siguiente patrón de números llegando hasta el
#número elegido:

print ("Ingrese número:")

numingresado = int (input ())

if numingresado <= 0:
     print ("Error")
else:
 for i in range (1, numingresado+1):
    for j in range (1, i+1):
     print (j, end="")
    print ()

    