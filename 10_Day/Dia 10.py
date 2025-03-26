#Ejercicios dia 10
#Programa 1
#for
print ("programa 1:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print ('bucle for: ', numero)
#while
cont = 0
while cont <= 10:
    print('bucle while: ', cont)
    cont = cont + 1

#Programa 2
print ("programa 2:")
numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for number in numbers:
    print ('bucle for: ', number)

cont = 10
while cont > -1:
    print('bucle while: ', cont)
    cont = cont -1

#Programa 3
print ("programa 3:")
for i in range (1, 8):
    print ("#" * i)

#Programa 4
print ("programa 4:")
e = '#'
for i in range (8):
    print (e * 8 )

#Programa 5
print ('programa 5:')
for i in range(11):
    print(f"{i} x {i} = {i * i}")

#Programa 6
print ("programa 6:")
herramientas = ['Python', 'Numpy','Pandas','Django', 'Flask']
for herramienta in herramientas:
    print (herramienta)

#Programa 7
print ("programa 7:")
for i in range (101):
    if i % 2==0:
        print (i)

#Programa 8
print ("programa 8:")
for i in range (101):
    if i % 2!=0:
        print (i)

#Ejercicios nivel 2
#programa 1
print ("programa 1, nivel 2:")
sumaTotal = 0
for i in range (101):
    sumaTotal += i
print ("La suma total es: ", sumaTotal)

#Programa 2
print ("programa 2, nivel 2:")
sumaPares = 0
sumaImpares = 0
for i in range (101):
    if i % 2== 0:
        sumaPares += i
    else:
        sumaImpares += i
print ("La suma de los pares es: ", sumaPares)
print ("La suma de los impares es: ", sumaImpares)


#Ejercicios nivel 2
#Programa 1
print ("programa 1, nivel 3:")
import paises as p
paises = p.countries
land = 'land'
for pais in paises:
    if land in pais:
        print (pais)

#Programa 2
print ("programa 2, nivel 3:")
fruitsList = ['banana', 'orange', 'mango', 'lemon']
print (fruitsList)
reverseFruits = []
for fruit in fruitsList [::-1]:
    reverseFruits.append(fruit)
print (reverseFruits)

#Programa 3
print ("programa 3, nivel 3:")
import countriesData as countrie
paisData = countrie.paisD
lenguajes = []
for pais in lenguajes:
    for lenguaje in pais:
        lenguajes.append("languages")

print (lenguajes)



