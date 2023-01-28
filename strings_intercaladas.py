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


