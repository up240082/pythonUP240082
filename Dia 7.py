#Ejercicios dia 7

#Programa 1
print ('programa 1:')
it_companies = ('Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazo')

#Programa 2
print ('programa 2:')
add = ('twitter',)
it_companiesDos = it_companies + add
print (it_companiesDos)

#Programa 3
print ("programa 3:")
empresasDigitales = ('snapchat', 'tiktok', 'instagram')
it_companiesTres = (it_companiesDos + empresasDigitales)
print (it_companiesTres)

#Programa 4
print ('programa 4:')
print (it_companiesTres[1:11])

#Programa 5
print ('programa 5:')
#Retirar (remove) implica sacar un elemento de una lista
#Desechar elimina un elemento solo si esta presente, si no lo esta, no lanza error

#Ejercicios nivel 2
#Programa 1
print ("programa 1, nivel 2:")
A = ['19', '22', '24', '20', '25', '26']
B = ['19', '22', '20', '25', '26', '24', '28', '27']
AB = A + B
print (AB)

#Programa 2
print ('programa 2, nivel 2:')
A = {'19', '22', '24', '20', '25', '26'}
B = {'19', '22', '20', '25', '26', '24', '28', '27'}
print (A.intersection(B))

#Programa 3
print ("programa 3, nivel 2:")
A = {'19', '22', '24', '20', '25', '26'}
B = {'19', '22', '20', '25', '26', '24', '28', '27'}
print ("Es A subconjunto de B?: " ,A.issubset(B))
print (A.issuperset(B))

#Programa 4
print ("programa 4, nivel 2:")
A = {'19', '22', '24', '20', '25', '26'}
B = {'19', '22', '20', '25', '26', '24', '28', '27'}
print (A.isdisjoint(B))

#Programa 5
print ("programa 5, nivel 2:")
A = ['19', '22', '24', '20', '25', '26']
B = ['19', '22', '20', '25', '26', '24', '28', '27']
BA = B + A
print ("A + B: ",AB)
print ("B + A",BA)

#Programa 6
print ("programa 6, nivel 2:")
A = {'19', '22', '24', '20', '25', '26'}
B = {'19', '22', '20', '25', '26', '24', '28', '27'}
print (A.symmetric_difference(B))


#Programa 7
print ("programa 7, nivel 2:")
AB.clear()
BA.clear()
print (AB + BA)

#Ejercicios nivel 3
#Programa 1
print ("programa 1, nivel 3:")
ages = ['22', '19', '24', '25', '26', '24', '25', '24']
ages_set = set(ages)
print (ages_set)
if len(ages) > len(ages_set):
    print ("La lista es mayor")
else:
    print ("El conjunto es mayor")    
    

#Programa 2
print ("programa 2, nivel 3:")



#Programa 3
print ("programa 3, nivel 3:")
frase = "I am a teacher and I love to inspire and teach people"
