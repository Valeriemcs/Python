
def repetidos(lista):
    resultado=[]
 
    for i in lista:
       
        if (lista.count(i)<=1):
          
            resultado.append(i)
 
    return resultado

lista_numeros=[20, 30, 40, 20, 5, 100, 5, 20]
lista_palabras=["perro", "gato", "perro", "mapache"]
print(sorted(repetidos(lista_numeros)))
print(sorted(repetidos(lista_palabras)))
