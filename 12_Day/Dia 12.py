def calcular_modo(numeros):
    from collections import Counter
    frecuencias = Counter(numeros)
    max_frecuencia = max(frecuencias.values())
    modos = [num for num, freq in frecuencias.items() if freq == max_frecuencia]
    return modos

# Lista de números
numeros = [4, 5, 6, 4, 7, 4]

# Calcular y mostrar el modo
modos = calcular_modo(numeros)
print(f"El modo es: {modos}")