# Cree una función que cuente todas las apariciones de cada caracter en una
# string; esta string debe recibirse como parámetro. El resultado debe ser un
# diccionario y debe ser impreso en pantalla.

#Se crea la función y se inicializan variables.
def apariciones(cadena):

    #Aquí las letras se guardan en forma de diccionario.
    letras = dict()
    contador = 0 #Aquí se cuenta la cantidad de veces repetido.

#Se abre un for que compara si la letra ya se encuentra en la lista si no se agrega a letras para que inicie el diccionario y se suma un contador
#de esa letra, si ya se encuentra en diccionario solo se suma al contador.
    for i in cadena: 
        if i in letras: 
            if letras[i] == 1: 
                contador += 1 
            letras[i] += 1 
        else:
            letras[i] = 1   
    print (letras)
           
    return letras, contador
    
#casos de prueba
texto1= ("papaya")
texto2= ("asdsvsdsdaj")
texto3= ("12324335434")
texto4= ("")
texto5= ("%&/((#/))")

#Llama a la función
#cambiar a texto1,texto2,texto3, texto4 y texto5 dentro del parentesis para hacer las pruebas.
resultado = apariciones(texto1)

