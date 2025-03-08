#Ejerciciso dia 4

#Programa 1
print ("programa 1:")
listaVacia = []
print (listaVacia)

#Programa 2
print ("programa 2:")
lista = ('banana', 'apple', 'orange', 'lemon', 'mango')
print (lista)

#Programa 3
print ("programa 3:")
print (len(lista))

#Programa 4
print ("programa 4:")
print (lista[0])
print (lista[2])
print (lista [4])


#Programa 5
print ("programa 5:")
mixed_data_types = 'Alejandro', '18', '1.77m', 'Casado', 'Paseo San Gerardo #150'



#Programa 6
print ("programa 6:")
it_companies =  ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


#Programa 7
print ("programa 7:")
print (it_companies)
print (mixed_data_types)

#Programa 8
print ("programa 8:")
print (len(it_companies))

#Programa 9
print ("programa 9:")
print (it_companies[0])
print (it_companies[3])
print (it_companies[6])

#Programa 10
print ("programa 10:")
it_companiesDos =   ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companiesDos [0] = 'Twitter'
print (it_companiesDos)

#Programa 11
print ("programa 11:")
it_companiesTres =  ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companiesTres.append('Snapchat')
print (it_companiesTres)

#Programa 12
print ("programa 12:")
it_companiesTres.insert (4, 'Instagram')
print (it_companiesTres)

#Programa 13
print ("programa 12:")
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
mayus = it_companies[3].upper()
print (mayus)

#Programa 14
print ("programa 14:")
print ('#'.join(it_companies))


#Programa 15
print ("programa 15:")
comparar = 'Apple' in it_companies
print (comparar)

#Programa 16
print ("programa 16:")
it_companies.sort()
print (it_companies)


#Programa 17
print ("programa 17:")
it_companies.reverse()
print (it_companies)

#Programa 18
print ("programa 18:")
cutCompanies = it_companiesTres[3:9]
print (cutCompanies)

#Programa 19
print ("programa 19:")
cutCompanies = it_companiesTres[0:6]
print (cutCompanies)

#Programa 20
print ("programa 20:")
cutCompanies = it_companiesTres[0:4]+it_companiesTres[5:9]
print (cutCompanies)

#Programa 21
print ("programa 21:")
del it_companiesTres[0]
print (it_companiesTres)

#Programa 22
print ("programa 22:")
del it_companiesTres[5]
print (it_companiesTres)


#Programa 23
print ("programa 23:")
del it_companiesTres[6]
print (it_companiesTres)


#Programa 24
print ("programa 24:")
del it_companiesTres[0:6]
print (it_companiesTres)

#Programa 25
print ("programa 25:")
it_companiesTres.clear()
print (it_companiesTres)

#Programa 26
print ("programa 26:")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
listaFinal = front_end + back_end
print (listaFinal)


#Programa 27
print ("programa 27:")
inserta= ['python', 'SQL']
listaFinalDos = listaFinal + inserta
print (listaFinalDos)

#Ejercicios Nivel 2
#Programa 1
print ("Programa 1, NIVEL 2:")
#Ordena las edades
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort ()
print ("La lista ordenada: ", ages)
#Encontrar la edad minima y maxima
edadMinima = min(ages)
edadMaxima = max(ages)
print ("La edad minima es: ", edadMinima)
print ("La edad maxima es: ", edadMaxima)
#Agregar la minima y la maxima a la lista
ages.append(edadMaxima)
ages.append(edadMinima)
print ("La lista con la min y la max agregada es: ", ages)
#Edad media
mediana = (ages[4]+ages[5]/2)
print('La media es:', mediana)
#Promedio
promedio = (sum(ages)/len(ages))
print ("El promedio es: ", promedio)
#ya no le supe
comparacion =(ages[0]-promedio) and (ages[-1]-promedio)
print('El resultado de la comparacion es:',comparacion)


#Programa 2 
print ("programa 2, NIVEL 2: ")
import countries as p
paises = p.countries
print(len(paises))
