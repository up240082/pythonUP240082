#Ejercicios dia 13
#Programa 1
print ("programa 1:")
listaNumeros = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
numF = [num for num in listaNumeros if num >=0]
print(numF)

#Programa 2
print ("programa 2:")
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista = [num for i in list_of_lists for j  in i for num in j]
print (lista)

#Programa 3
print ("programa 3:")
tuplesList = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print  (tuplesList)