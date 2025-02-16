# Estilo Lógico (sin Prolog, usando una solución basada en reglas matemáticas y listas por comprensión)
# En este enfoque, aplicamos una solución lógica similar a la "Criba de Eratóstenes".

def primos_logico(n):
    if n < 2:
        return []
    numeros = list(range(2, n + 1))
    for i in numeros:
        numeros = [x for x in numeros if x == i or x % i != 0]
    return numeros

# Uso de los estilos
num = int(input("Ingrese un número: "))

print("Lógico:", primos_logico(num))