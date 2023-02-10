
def contar_carac (cadena):
    num = 0
    letras= 0
    especiales= 0

    for i in cadena:
        if i.isdigit ():
            num += 1
        elif i.isalpha():
            letras += 1
        else:
            especiales += 1

    return num, letras, especiales

texto= input ("Digite un texto: ")
resultado = contar_carac(texto)

print ("Cantidad de números: %i  " % resultado [0]) 
print ("Cantidad de letras: %i  " % resultado [1]) 
print ("Cantidad de caracteres especiales: %i  " % resultado [2]) 