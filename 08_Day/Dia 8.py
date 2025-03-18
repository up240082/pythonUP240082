#Ejercicios dia 8
#Programa 1
print ("programa 1:")
perro = {}

#Programa 2
print ("programa 2:")
perro ['nombre'] = 'toby'
perro ['color'] = 'cafe'
perro ['raza'] = 'chihuahua'
perro ['patas'] = '4'
perro ['edad'] = '5 años'
print (perro)

#Programa 3
print ("programa 3:")
estudiante = {
    'nombre': 'Alejandro',
    'apellido': 'Lopez',
    'sexo': 'masculino',
    'edad': '18',
    'Estado civil': 'soltero',
    'Habilidades':['veloz', 'inteligente'],
    'Pais': 'Italia',
    'ciudad': 'Aguascalientes',
    'Direccion':{
        'Calle':'Paseo San Gerardo',
        'Colonia':'San Gerardo'}}
print (estudiante)

#Programa 4
print ("programa 4:")
print (len(estudiante))

#Programa 5
print ("programa 5:")
print (estudiante['Habilidades'])
print (type(estudiante['Habilidades']))

#Programa 6
print ("programa 6")
estudiante['Habilidades'].append ('tomar')
print (estudiante)

#Programa 7
print ('programa 7:')
keys = estudiante.keys()
print (keys)

#Programa 8
print ("programa 8:")
values = estudiante.values()
print (values)

#Programa 9
print ("programa 9:")
items = estudiante.items()
print (items)

#Programa 10
print (estudiante.pop('ciudad'))

#Programa 11
print ('programa 11:')
del estudiante

