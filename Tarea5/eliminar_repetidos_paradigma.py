##Con paradigma
##
##

from functools import reduce

# función para eliminar elementos repetidos de una lista
##acc representa la lista donde se van acumulando los valores que no estan repetidos
def eliminar_repetidos(lista):
    return reduce (lambda acc, i: acc + [i] if i not in acc else acc, lista, [])#aqui el i es el recorrido con la lista de los números repetidos
    #que se van metiendo a la lista acc si no estan en ella.


# Ejemplos con listas
listauno = [1, 2, 3, 3, 2, 4, 6]
listados = [3, 3, 3, 3, 3, 3, 3]
listatres = []

resultado_uno = eliminar_repetidos(listauno)
resultado_dos = eliminar_repetidos(listados)
resultado_tres = eliminar_repetidos(listatres)

print(resultado_uno)
print(resultado_dos)
print(resultado_tres)

## Antes de usar paradigma (Original)
##
##
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