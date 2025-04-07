#Ejercicios dia 12
#Programa 1
print ("programa 1:")
import random
import string
def randomUserId ():
    return ''.join(random.choices(string.ascii_letters + string.digits, k= 6))
print('usuario generado: ', randomUserId())

#Programa 2
print ("programa 2:")
def userIdGenByUser():
    numCarac = int(input("ingresa el numero de caracteres: "))
    numIds = int(input("ingresa el numero de ids: "))
    ids = [
        ''.join(random.choices(string.ascii_letters + string.digits, k=numCarac))
        for _ in range (numIds)
    ] 
    return ids
print (userIdGenByUser())

#Programa 3
print ("programa 3:")
def rgbColorGen():
    verde = random.randint(0,255)
    azul = random.randint(0,255)
    rojo = random.randint(0,255)
    return (verde,azul,rojo)
print (rgbColorGen())

#Programas Nivel 2
print ("programa 1, nivel 2:")
import random
def listaDeColoresHexa(n):
    return ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(n)]
hexaColor = listaDeColoresHexa(8)
print ("colores generados: ", hexaColor)

#Programas nivel 2
print ("programa 2, nivel 2:")
def listOfRgbColors():
    return [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for _ in range(n)]

#Programa nivel 2
print ("programa 3, nivel 2:")
def generarColores(color_type, n):
    return ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(n)] if color_type == 'hexa' else [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(n)] if color_type == 'rgb' else "Error: Usa 'hexa' o 'rgb'."
print (generarColores('hexa', 5))
print (generarColores('rgb', 5))

#Programa nivel 3
print ("programa 1, nivel 3:")
def shuffleList(lst):
    random.shuffle(lst)
    return lst
miLista = [5,6,7,8,9,10]
print("lista revuelta: ", shuffleList(miLista))

#Programa nivel 3
import random
print ("programa 2, nivel 3:")
def uniquesNumbers():
    return random.sample(range(10),7)
randomNumbers = uniquesNumbers()
print ("numeros aleatorios unicos: ", randomNumbers)
print("revisado")