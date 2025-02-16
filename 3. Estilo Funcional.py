# Estilo Funcional
# Se utiliza programación funcional con "filter" y "all" para calcular los primos de forma declarativa.
from functools import reduce

# Función funcional para verificar si un número es primo
def es_primo_funcional(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# Función para obtener todos los números primos hasta un número dado usando programación funcional
def primos_funcional(n):
    return list(filter(es_primo_funcional, range(2, n + 1)))

# Uso de los estilos
num = int(input("Ingrese un número: "))

print("Funcional:", primos_funcional(num))