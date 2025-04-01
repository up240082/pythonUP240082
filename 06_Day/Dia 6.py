#Ejercicios dia 6

#Programa 1
print ("programs 6:")
tuple = ()
print (tuple)

#Programa 2
print ("programa 2:")
tupleHermano = ("Brian",)
tupleHermana = ("Amy", "Andy")


#Programa 3
print ("programa 3:")
hermanos = tupleHermano + tupleHermana
print (hermanos)


#Programa 4
print ("programa 4:")
totalHermns = len(hermanos)
print ("El total de hermanos que tengo es de: ", totalHermns)

#Programa 5
print ("programa 5:")
padres = ("Maria", "Aaron")
familyMembers= padres + hermanos
print (familyMembers)

#Ejercicios nivel 2
#Programa 1
print ('programa 1:')
unPack = familyMembers [0:2]
print (unPack)
unPackDos = familyMembers [2:6]
print (unPackDos)

#Programa 2
print ('programa 2:')
fruits = ('manzana', 'pera', 'naranja')
vegetables = ('lechuga', 'jitomate', 'zanahoria')
animals = ('jp', 'cebra', 'leon')
food_stuff_tp = fruits + vegetables + animals
print (food_stuff_tp)

#Programa 3
print ('programa 3:')
food_stuff_it = ('manzana', 'pera', 'naranja', 'lechuga', 'jitomate', 'zanahoria', 'jp', 'cebra', 'leon')
print (food_stuff_it)

#Programa 4
print ('programa 4:')
print ('nueva lista: ', food_stuff_it[0:3]+ food_stuff_it[5:9])

#Programa 5
print ("programa 5:")
print ('nueva lista: ', food_stuff_it[3:6])

#Programa 6
print ('programa 6:')
del food_stuff_tp

#Programa 7
print ('programa 7:')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
comprueba = ('estonia' in nordic_countries)
compruebaDos = ('Iceland' in nordic_countries)
print ("Estonia se encuentra en la lista?: ", comprueba)
print ("iceland se encuentra en la lista?: ", compruebaDos)


print("Revisado")