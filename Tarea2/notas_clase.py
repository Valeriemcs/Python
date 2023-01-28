#Notas de clase: Dado el siguiente diccionario, escriba un programa que
#imprima en pantalla el promedio de notas del estudiante. Debe imprimirlo en
#un diccionario de la forma {"nombre": 75}

sampleDict = {
    "class": {
      "student": {
       "name": "Mike",
     "marks": {
      "physics": 70,
      "history": 80,
      "math": 90
            },
        }
    }
}


i= 0
j= 0
for materia, nota in sampleDict["class"]["student"]["marks"].items():
          i  += nota   
j = i// 3
print ("", (sampleDict["class"]["student"]["name"]),":", j)            
