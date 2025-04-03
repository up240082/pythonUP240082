#Ejercicios dia 14
#Programa 1
print ("programa 1:")
# map transforma cada elemento, filter selecciona elementos basados en una condicion y reduce combina los elemtnso en un unico valor

#Programa 2
print ("programa 2:")
# las funciones de orden superior manejan funciones como argumentos o retornos
# los clousures retienen variables del entorno en el que fueron definidas
# los decoradores modifican funciones dinamicamente sin alterar su codigo original

#Programa 3
print ("programa 3:")
from functools import reduce
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))

#Programa 4
print ("programa 4:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for countrie in countries:
        print (countrie)

#Programa 5
print ("programa 5:")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
      print (name)

#Programa 6
print ("programa 6:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
      print (number)

#Ejercicios nivel 2
#Programa 1, nivel 2
print ("programa 1, nivel 2:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
uppercaseCountries = list(map(str.upper, countries))
print (uppercaseCountries)

#Programa 2, nivel 2
print ("programa 2, nivel 2:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def alCuadrado (n):
      return n ** 2
r = map(alCuadrado, numbers)
print (list(r))

#Programa 3, nivel 2
print ("programa 3, nivel 2:")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
upperCaseNames = list(map(str.upper, names))
print (upperCaseNames)

#Programa 4, nivel 2
print ("programa 4, nivel 2:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def land (countrie):
      if 'land' in countrie:
            return True
      return False
r = filter(land, countries)
print(list(r))

#Programa 5, nivel 2
print ("programa 5, nivel 2:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def six (countrie):
      if len(countries) == 6:
            return True
      return False
r = filter (six, countries)
print (list(r))

#Programa 6, nivel 2
print ("programa 6, nivel 2:")
def sixOrMore(countrie):
      if len(countries) >= 6:
            return True
      return False
r = filter(sixOrMore, countries)
print (list(r))

#Programa 7, nivel 2
print ("programa 7, nivel 2:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def starWhit (countrie):
    return countrie.startswith("E")
r = filter(starWhit,countries)
print(list(r))

#Programa 8, nivel 2
print ("programa 8, nivel 2:")
from functools import reduce
arr = [1, 2, 3, 4, 5, 6]
mapped = map(lambda x: x * 2, arr)
filtered = filter(lambda x: x > 5, mapped)
result = reduce(lambda x, y: x + y, filtered)
print(result)

#Programa 9, nivel 2
print ("programa 9, nivel 2:")
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
mixed_list = [42, "hello", 3.14, "world", True, "Python"]
string_list = get_string_lists(mixed_list)
print(string_list)

#Programa 10, nivel 2
print ("programa 10, nivel 2:")
def suma(x,y):
      return int(x) + int(y)
print(reduce(suma,numbers))

#Programa 11, nivel 2
def concatenarPaises(a,b):
     if a == "Estonia, Finland, Sweden, Denmark, Norway" and b == "Iceland":
          return a + ", and" + b
     else:
          return a + ", " + b
print (reduce(concatenarPaises,countries )+ "are north European countries")

#Programa 12, nivel 2
print("programa 12, nivel 2:")
import paises as p
paises = p.countries
print (list(filter(land, paises)))

#Programa 13, nivel 2
print ("programa 13, nivel 2:")
keys = []
keys = [i[0] for i in paises if i[0] not in keys]
def contarcountry(contador):
    return sum([True for i in paises if i[0].startswith(contador)])
values = [contarcountry(l) for l in keys]
print(dict(zip(keys, values)))

#Programa 14, nivel 2
print ("programa 14, nivel 2:")
def getFirstTenCountries():
     return paises[:10]
print (getFirstTenCountries())

#Programa 15, nivel 2
print ("programa 15, nivel 2:")
def getLastTenCountries():
     return paises[-10:]
print (getLastTenCountries())