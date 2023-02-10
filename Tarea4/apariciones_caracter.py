
def apariciones(cadena):

    letras = dict()  #Guarda repetición de letras
    contador = 0 #Caracteres que se repiten

    for i in cadena: 
        if i in letras: 
            if letras[i] == 1: 
                contador += 1 
            letras[i] += 1 
        else:
            letras[i] = 1 
    print (letras)
           
    return letras, contador
    

texto= input ("Digite un texto: ")
resultado = apariciones(texto)

