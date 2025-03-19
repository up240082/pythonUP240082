#Ejercicios dia 9

#Programa 1
print ('programa 1:')
edad = int(input("Ingresa tu edad: "))
if edad > 17:
    print ("Puedes manejar")
else:
    print ("No puedes manejar")

#Programa 2
print ('programa 2:')
miEdad = int(input("Ingresa mi edad: "))
tuEdad= int(input("Ingresa tu edad: "))
if miEdad > tuEdad:
    print ("Mi edad es mayor: ", miEdad-tuEdad)
elif miEdad == tuEdad:
    print ("Son la misma edad: ")
else:
    print ("Tu edad es mayor: ", miEdad-tuEdad)

#Programa 3
print ("programa 3:")
a = int(input("Ingresa el primer numero: " ))
b = int(input("Ingresa el segundo numero: "))
if a > b:
    print ("El numero 'a' es mayor: ")
elif a == b:
    ("Los numeros son iguales: ")
else:
  print  ("El numero 'b' es mayor: ")

#Ejercicios nivel 2
#Programa 1
print ("programa 1:")
alumno = int(input("Ingrese la calificacion del alumno: "))
if alumno > 79 and alumno < 100:
    print ("El alumno tiene un 'A'")
elif alumno > 69 and alumno < 80:
    print ("El alumno tiene una 'B'")
elif alumno > 59 and alumno < 70:
    print ("El alumno tiene una 'C'")
elif alumno > 49 and alumno < 60:
    print ("El alumno tiene una 'D'")
else:
    print ("El alumno tiene una 'F'")

#Programa 2
print ("programa 2:")
mes = (input("Ingresa el  mes: "))
if mes in ['septiembre', 'octubre', 'noviembre',]:
    print ("La estacion es otoño")
elif mes in ['diciembre', 'enero', 'febrero',]:
    print ("La estacion es invierno")
elif mes in ['marzo','abril', 'mayo',]:
    print ("La estacion es primavera")
else:
    print ("La estacion es verano")

#Programa 3
print ("programa 3:")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruta = str(input("Ingresa la fruta: "))
if fruta in fruits:
    print ("La fruta esta en la lista")
else:
    fruits.append(fruta)
    print (fruits)

#Ejercicios nivel 3
#Programa 1