
# #Utilizando Paradigma
from functools import reduce

def factorial(num):
    if num < 0: #realiza validación para comprobar que no son negativos
        return "No se pueden sacar factoriales de números negativos"
    else: #Si son positivos empeza a calcular factorial
        return reduce(lambda x, y: x*y, range(1, num+1)) #recorre los numeros para llegar al numero ingresado o x en este caso y los va multiplicando

num_ingresado = 10 #Cambiar número para hacer otras pruebas
resultado = factorial(num_ingresado)
print(f"El factorial de {num_ingresado} es: {resultado}")



#Sin Paradigma (Original)
#Factorial del número dado: Escriba un programa en el que dado un número
#por el usuario, imprima el factorial (!) de dicho número.
#Prueba
numingresado = 5 #cambiar el número para hacer mas pruebas
fact = 1
for i in range (1, numingresado+1):
        fact*=i

if numingresado <= 0:
  print ("No se pueden sacar factoriales de números negativos")
else: 
  print (" El factorial de", numingresado, "es: ", fact) 

