# Cree una función que cuente e imprima en pantalla todos los números,
# letras y caracteres especiales presentes en una string. Debe recibir esta
# string por parámetro.

def contar_carac (cadena):  #se crea la función y se inicializan variables
    num = 0
    letras= 0
    especiales= 0

#se crea un for para contar cuando es digito, letra y el else es la excepción por lo tanto los caracteres 
#especiales entran en esta categoria por defecto
    for i in cadena: 
        if i.isdigit ():
            num += 1
        elif i.isalpha():
            letras += 1
        else:
            especiales += 1

    return num, letras, especiales

#casos de prueba
texto1= ("()))()/(&)")
texto2= ("P@#yn26at^&i5ve")
texto3= ("1232342343435")
texto4= ("fjsdfjd")

#Llama a la función
#cambiar a texto1,texto2,texto3 y texto cuatro dentro del parentesis para hacer las pruebas.
resultado = contar_carac(texto1)

#Esto es para que se impriman los resultados
print ("Cantidad de números: %i  " % resultado [0]) 
print ("Cantidad de letras: %i  " % resultado [1]) 
print ("Cantidad de caracteres especiales: %i  " % resultado [2]) 
