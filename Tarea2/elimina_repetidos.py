
#Elimina repetidos: Crea un programa que elimine los elementos repetidos
#de una lista.

listauno = [1, 2, 3, 3, 2, 4, 6]
listados= [3, 3, 3, 3, 3, 3, 3]
listatres= []

#Se crea variable resultado, declarandola lista. Esto para que el for recorra la lista y vaya depositando los numeros en la lista "resultado"
#si el número a depositar en la variable resultado ya existe no lo deposita.
resultado = []
for i in listauno:
    if i not in resultado:
        resultado.append(i)
print (resultado)

resultado = []
for i in listados:
    if i not in resultado:
        resultado.append(i)
print (resultado)

resultado = []
for i in listatres:
    if i not in resultado:
        resultado.append(i)
    print (resultado)
else:
  print ("Error") 