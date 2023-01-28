#Strings intercaladas: Escriba un programa que reciba dos strings del mismo
#largo por parte del usuario e imprima una nueva string con los caracteres de
#ambos inputs intercalados.

print ("Ingrese la primera palabra: ")
primera = input()

print ("Ingrese la segunda palabra: ")
segunda =  input()

print ("Las palabras son",  primera, "y" ,  segunda)

i =0
intercalada = ""

while (i < len (primera)):
    intercalada += primera[i] + segunda[i]
    i = i+1
print (intercalada)


