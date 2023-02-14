# Escriba una función que elimine todas las apariciones de un elemento en una
# lista. Tanto la lista como el valor que se quiere eliminar deben ser parámetros
# de la función.

#Se crea función y se inicia la variable en lista
def repetidos(lista):
    resultado=[]

#Se crea un for en el que compara con el comando .count si el numero de veces en que aparecen los elementos elementos es igual a uno o menos
#si el elemento aparece una sola vez agrega este elemento a la lista y si aparece más de una vez no lo agrega y por lo tanto se elimina.
    for i in lista:
       
        if (lista.count(i)<=1):
          
            resultado.append(i)
    print (resultado)
    return resultado
 
#Casos de prueba 
lista1=[20, 30, 40, 20, 5, 100, 5, 20] 
lista2=["perro", "gato", "perro", "mapache"]
lista3 =["Arroz", "Patata", "Pato", "Ámbar"]
lista4= [""]

#Llama a la función
#cambiar a lista1, lista2, lista3 y lista4 dentro del parentesis para hacer las pruebas.
resultado = repetidos(lista1)