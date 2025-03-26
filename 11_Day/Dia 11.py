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
#Programa 7
print ("programa 7:")

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
