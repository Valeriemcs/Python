#SUMA
#

def suma(lista):
    res= 0
    for i in lista:
        res = res + i
    return res

lista = []
valor = float(input ("Ingrese Número: (ingrese 0 si quiere dejar de agregar)"))

while valor!= 0:
    lista.append(valor)
    valor=float(input("Ingresa valor 0 para finalizar:"))
    
    
print ("El resultado es:" + str(suma(lista)))
print  (lista)

# MULTIPLICACIÓN
#
def multi(lista):
    res = 1
    for i in lista:
        res *= i
    return res

lista = []
valor = float(input ("Ingrese Número: (ingrese 0 si quiere dejar de agregar)"))

while valor!= 0:
    lista.append(valor)
    valor=float(input("Ingresa valor 0 para finalizar:"))

print ("El resultado es:" + str(multi(lista)))

#POTENCIA
#
def poten(x,y):
    return pow (x,y)

num = 1

for i in range (0,num):
    base = int (input("Por favor ingrese la base:"))
    exponente = int (input("Por favor ingrese el exponente:"))

    print (str(base) + " elevado a " +" "+ str(exponente) + " es = " + str(poten(base,exponente)))