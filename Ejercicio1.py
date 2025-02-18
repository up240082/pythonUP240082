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








