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


