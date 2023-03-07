##Con Paradigma
##
def intercalar_strings(str1, str2): #Se definen las cadenas o palabras
    return ''.join([char1+char2 for char1, char2 in zip(str1, str2)])
#Se utiliza la funcion "join" que sirve para unir en una 
#sola string varios caracteres y la zip para iterar la string 1 y 2 simultaneamente.

#Cambiar las palabras si se quiere hacer más pruebas
primera = "pala"
segunda = "mesa"

print(f"Las palabras son {primera} y {segunda}")
intercalada = intercalar_strings(primera, segunda)
print(intercalada)

## Sin usar paradigmas (Original)
#Strings intercaladas: Escriba un programa que reciba dos strings del mismo
#largo por parte del usuario e imprima una nueva string con los caracteres de
#ambos inputs intercalados.


primera = "paz"
segunda =  "oso"

print ("Las palabras son",  primera, "y" ,  segunda)

i =0
intercalada = ""

while (i < len (primera)):
    intercalada += primera[i] + segunda[i]
    i = i+1
print (intercalada)

