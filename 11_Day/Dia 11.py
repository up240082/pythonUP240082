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
    