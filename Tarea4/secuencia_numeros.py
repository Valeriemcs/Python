# Cree una función que reciba una secuencia de números separados por coma
# por parte del usuario e imprima una lista y una tupla que contengan dichos
# valores. El usuario debe ingresar un único input con los valores separados
# por comas.

#Función y variable inicializada
def secuencia(listas):
    resultado =  ()  
    
#variables para recibir los números dados, el .split divide los numeros separados por espacio y los separa
#aún así si el usuario los separa el mismo funciona, tuple es para hacer la lista en tupla. luego se imprimen ambos resultados
    recibe = numeros.split()
    recibe_tupla =tuple(recibe)
    print (recibe)
    print (recibe_tupla)
    return resultado

#El caso decía que se deben recibir los números por usuario así que se realizó por medio de un input
numeros= input ("Digite los números que desea separados por una coma: ")
resultado_final = secuencia(numeros)
