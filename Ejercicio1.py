# Dia 3
edad = 18
print (type(edad))
altura = 1.78
print (type(altura))
numeroComplejo =4j
print(type(numeroComplejo))

# area de un triangulo - Programa 4
alturaTriangulo = float(input("ingresa la altura del triangulo: "))
print (type(alturaTriangulo))
baseTriangulo = float(input("ingresa la base del triangulo: "))
print (type(baseTriangulo))
areaDelTriangulo = 0.5 * (baseTriangulo * alturaTriangulo)
print ("el area del triangulo es de: ", areaDelTriangulo)

# Perimetro del triangulo - programa 5
primerLado = float(input("ingrese el primer lado del triangulo: "))
print(type(primerLado))
segundoLado = float(input("ingrese el segundo lado del triangulo: "))
print(type(segundoLado))
tercerLado = float(input("ingrese el tercer lado del triangulo: "))
print(type(tercerLado))
perimetroDelTriangulo = primerLado + segundoLado + tercerLado
print ("el perimetro del triangulo es de: ", perimetroDelTriangulo)

# Area y perimetro de un rectangulo - Programa 6
longitudRectangulo = float(input("ingrese la longitud del rectangulo: "))
print(type(longitudRectangulo))
anchuraRectangulo = float( input("ingrese la anchura del rectangulo: "))
print(type(anchuraRectangulo))
areaDelRectangulo = longitudRectangulo * anchuraRectangulo
perimetroDelRectangulo = 2 * (longitudRectangulo + anchuraRectangulo)
print ("el area del rectangulo es de: ", areaDelRectangulo)
print ("el perimetro del rectangulo es de: ", perimetroDelRectangulo)

# Area del circulo - Programa 7
radio = float(input("ingrese el radio del circulo: "))
print (type(radio))
pi = 3.1416
areaOfCircle = pi * radio **2
circumOfCircle = 2 * pi * radio
print ('el area del circulo es: ', areaOfCircle)
print ('la circuferencia del circulos es: ', circumOfCircle)

# Pendiente, intersección con el eje x e intersección con el eje y de y = 2x - 2
# Programa 8
pendiente = 2
interseccion_y = -2
# Para la intersección con el eje x
interseccion_x = -interseccion_y / pendiente
print("La pendiente es:", pendiente)
print("La intersección con el eje y es:", interseccion_y)
print("La intersección con el eje x es:", interseccion_x)

#Programa 9
import math
# Coordenadas de los puntos
x1, y1 = 2, 2
x2, y2 = 6, 10
# Calcular la pendiente
pendiente = (y2 - y1) / (x2 - x1)
# Calcular la distancia euclidiana
distancia_euclidiana = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("La pendiente es:", pendiente)
print("La distancia euclidiana es:", distancia_euclidiana)

#Programa 10
#PendientePorHacer...

#Programa 11
def calculate_y(x):
    return x**2 + 6*x + 9
x_values = range(-10, 11)
y_values = [calculate_y(x) for x in x_values]
epsilon = 1e-10
x_zero = None
for x, y in zip(x_values, y_values):
    if abs(y) < epsilon:
        x_zero = x
        break
print("Valores de x:", list(x_values))
print("Valores de y:", y_values)
if x_zero is not None:
    print(f"El valor de x para el que y es 0 es: {x_zero}")
else:
    print("No se encontró un valor de x para el que y sea 0.")

#Programa 12
lonUno = 'python'
lonDos = 'dragon'
length1 = len(lonUno)
length2 = len(lonDos)
print(f"La longitud de '{lonUno}' es: {length1}")
print(f"La longitud de '{lonDos}' es: {length2}")
comparaResultados = length1 != length2
print(f"¿Las longitudes de '{lonUno}' y '{lonDos}' son diferentes?: {comparaResultados}")

#Programa 13
lonUno = 'python'
lonDos ='dragon'
tiene = ('on' in lonUno) and ('on' in lonDos)
print (f"La silaba 'on' se encuentra en ambas palabras? ", tiene)

#Programa 14
oracion = "espero que este curso no este lleno de jerga"
jerga =("jerga" in oracion)
print (f"La palabra 'jerga' si se encuentra en la oracion?: ", jerga)

#Programa 15
lonUno: 'python'
lonDos: 'dragon'
noTiene= (not 'on' in lonUno) and (not 'on' in lonDos)
print (f"La silaba 'on' se encuentra en ambas palabras? ", noTiene)

#Programa 16
lonUno= 'python'
lonDos= (str(float(len(lonUno))))
print (f"la longitud de '{lonUno}'es: ", lonDos)











