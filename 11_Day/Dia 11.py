#Ejercicios dia 11
#Programa 1
print ("programa 1:")
def add_two_numbers():
    num_one = float(input("ingresa un numero: "))
    num_two = float(input("ingresa un numero: "))
    total = num_one + num_two
    print('resultado: ', total)
add_two_numbers()

#Programa 2
print ("programa 2:")
def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
rad =  float(input("ingrese el radio: "))
print(area_of_circle(rad))

#Programa 3
print ("programa 3:")
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total


#Programa 4
print ("programa 4:")
def convertirCelsiusAfarenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit
cel = float(input("ingrese los grados celsius: "))
print (convertirCelsiusAfarenheit(cel))

#Programa 5
print ("programa 5:")
def checkSeason(mes):
    primavera = ['marzo', 'abril', 'mayo']
    verano = ['junio', 'julio', 'agosto']
    otoño = ['septiembre', 'octubre', 'noviembre']
    invierno = ['diciembre', 'enero', 'febrero']
    
    if mes in primavera:
        return "Primavera"
    elif mes in verano:
        return "Verano"
    elif mes in otoño:
        return "Otoño"
    elif mes in invierno:
        return "Invierno"
    else:
        return "no esta mi apa"

month = input("Ingrese el mes: ")
print(checkSeason(month))

#Programa 6
print ("programa 6:")
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
x1 = float(input("ingrese x1: "))
y1 = float(input("ingrese y1: "))
x2 = float(input("ingrese x2: "))
y2 = float(input("ingrese y2: "))
print(calculate_slope(x1, y1, x2, y2))

#Programa 7
print ("programa 7:")
def solve_quadratic(a, b, c):
    x1 = (-b + ((b ** 2) - 4 * a * c) ** 0.5) / 2 * a
    x2 = (-b - ((b ** 2) - 4 * a * c) ** 0.5) / 2 * a
    return x1, x2
a = float(input("ingrese a: "))
b = float(input("ingrese b: "))
c = float(input("ingrese c: "))
print(solve_quadratic(a, b, c))

#Programa 8
print ("programa 8:")
def print_list(miLista):
    for elemento in miLista:
        print(elemento)

list= [100, 200, 300, 400, 500, 600]
print_list(list)

#Programa 9
print ("programa 9:")
def reverse_list(miLista):
    miLista.reverse()
    return miLista
list= [100, 200, 300, 400, 500, 600]
print(reverse_list(list))

#Programa 10
print ("programa 10:")
def capitalize_list_items(miLista):
    return [x.upper() for x in miLista]
list= ['hola', 'mundo', 'python']
print(capitalize_list_items(list))

#Programa 11
print ("programa 11:")
def add_item(miLista, item):
    miLista.append(item)
    return miLista
list= [1, 2, 3, 4, 5, 6]
item = 7
print(add_item(list, item))

#Programa 12
print ("programa 12:")
def remove_item(miLista, item):
    miLista.remove(item)
    return miLista
list= [1, 2, 3, 4, 5, 6]
item = 6
print(remove_item(list, item))

#Programa 13
print ("programa 13:")
def sum_of_numbers(n):
    if n < 1:
        return
    return sum(range(1, n + 1))
resultado = sum_of_numbers(10)
print("La suma total es:", resultado)

#Programa 14
print ("programa 14:")
def sum_of_odds(n):
    if n < 1:
        return
    return sum(range(1, n + 1, 2))
resultado = sum_of_odds(10)
print("La suma de los impares es:", resultado)

#Programa 15
print ("programa 15:")
def sum_of_evens(n):
    if n < 1:
        return
    return sum(range(2, n + 1, 2))
resultado = sum_of_evens(10)
print("La suma de los pares es:", resultado)
    

#Ejercicios nivel 2
#Programa 1
print ("programa 1, nivel 2:")
def evens_and_odds():
    numero = float(input("Ingrese un número: "))
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."
print(evens_and_odds())

#Programa 2
print("Programa 2, Nivel 2:")

def factorial(number):
    if number < 0:
        return "No está definido para números negativos."
    elif number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result
try:
    fac = int(input("Ingrese un número entero: "))
    print(f"El factorial de {fac} es: {factorial(fac)}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")


#Programa 3
print ("programa 3, nivel 2:")
def is_empty(valido):
    if not valido:
        return True
    else:
        return False
print (is_empty([]))
print (is_empty([1, 2]))

#Programa 4
print ("programa 4, nivel 2:")
def calculate_mean(lista):
    return suma(lista)/len(lista)
print (calculate_mean(lista=[1,2,3,4,5]))

def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 1:
        mediana = numeros_ordenados[n // 2]
    else:
        mediana = (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2
    return mediana
numeros = [1,2,3,4,5]
resultado = calcular_mediana(numeros)
print(f"La mediana es: {resultado}")

def calcular_mode(numeros):
    from collections import Counter
    frecuencias = Counter(numeros)
    max_frecuencia = max(frecuencias.values())
    modos = [num for num, freq in frecuencias.items() if freq == max_frecuencia]
    return modos
numeros = [4, 5, 6, 4, 7, 4]
modos = calcular_modo(numeros)
print(f"El modo es: {modos}")

def calcular_rango(numeros):
    return max(numeros) - min(numeros)
numeros = [4, 5, 6, 4, 7, 4]
rango = calcular_rango(numeros)
print(f"El rango es: {rango}")