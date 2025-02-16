# Dia 3
edad = 18
altura = 1.78
numeroComplejo = 18 + 4j

# area de un triangulo
seMultiplica = 0.5
alturaTriangulo = int(input("ingresa la altura del triangulo: "))
baseTriangulo = int(input("ingresa la base del triangulo: "))
areaDelTriangulo = seMultiplica * baseTriangulo * alturaTriangulo
print ("el area del triangulo es de: ", areaDelTriangulo)

# Perimetro del triangulo
primerLado = int(input("ingrese el primer lado del triangulo: "))
segundoLado = int(input("ingrese el segundo lado del triangulo: "))
tercerLado = int(input("ingrese el tercer lado del triangulo: "))
perimetroDelTriangulo = primerLado + segundoLado + tercerLado
print ("el perimetro del triangulo es de: ", perimetroDelTriangulo)

# Area y perimetro de un rectangulo
longitudRectangulo = int(input("ingrese la longitud del rectangulo: "))
anchuraRectangulo = int( input("ingrese la anchura del rectangulo: "))
areaDelRectangulo = longitudRectangulo * anchuraRectangulo
perimetroDelRectangulo = longitudRectangulo + anchuraRectangulo
print ("el area del rectangulo es de: ", areaDelRectangulo)
print ("el perimetro del rectangulo es de: ", perimetroDelRectangulo)

# Area del circulo
radio = int(input("ingrese el radio del circulo: "))
print (type(radio))
pi = 3.1416
areaOfCircle = pi * radio **2
circumOfCircle = 2 * pi * radio
print ('el area del circulo es: ', areaOfCircle)
print ('la circuferencia del circulos es: ', circumOfCircle)

# Calcular pendiente
x1 = 2
y1 = 2
x2 = 6
y2= 10
d = 0
pendienteDeLaRecta= y2-y1 / x2-x1
interseccionConElEjeY= pendienteDeLaRecta * d - x1
interseccionConElEjeX = (d + x1) / y1
pendienteEntreLosPuntos = (y2 - y1) / (x2 - x1)
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("pendiente de la recta y: ", pendienteDeLaRecta)
print ("interseccion con el eje y: ", interseccionConElEjeY)
print ("interseccion con el eje x: ", interseccionConElEjeX)
print ("pendiente entre los puntos: ", pendienteEntreLosPuntos)
print ("distancia entre los puntos, ", distancia)


