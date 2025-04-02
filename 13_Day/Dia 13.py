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
print(tuplesList)

#Programa 4
print ("programa 4:")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lista = [i for i in countries for j in i for i in j]
listaDos = [i.upper() for i in lista]
print (listaDos)

#Programa 5
print ("programa 5:")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
diccCountry = [{'country': country.upper(), 'city': city.upper() }for[(country, city)] in countries]
print (diccCountry)

#Programa 6
print ("programa 6:")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
listaa = [''.join(i)for j in names for i in j]
print (listaa)

#Programa 7
print ("programa 7:")
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
y_intercept = lambda m, x1, y1: y1 - m * x1
m = slope(1, 2, 3, 6)
b = y_intercept(m, 1, 2)
print("Slope:", m)
print("Y-Intercept:", b)