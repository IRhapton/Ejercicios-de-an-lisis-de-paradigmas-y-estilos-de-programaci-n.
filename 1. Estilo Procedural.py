# Estilo Procedural
# En este estilo, se utilizan funciones simples para dividir el problema en pasos básicos.
# Primero, verificamos si un número es primo y luego generamos una lista de primos hasta un límite.

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función para obtener todos los números primos hasta un número dado
def primos_hasta(n):
    return [i for i in range(2, n + 1) if es_primo(i)]

# Uso de los estilos
num = int(input("Ingrese un número: "))
print("Procedural:", primos_hasta(num))
