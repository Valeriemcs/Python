#Lista al cubo: Escriba un programa que cree una lista de números y la
#imprima. Luego debe imprimir dicha lista pero con cada valor convertido en
#su cubo.

lista = []


for i in range (5):
    numeros=int(input("Ingrese 5 números: "))
    lista.append(numeros **3)
print (lista)
   
