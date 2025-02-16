# Estilo Orientado a Objetos
# Aquí encapsulamos la lógica dentro de una clase para una mejor organización y reutilización del código.
# La clase "NumerosPrimos" almacena un límite y tiene métodos para verificar y generar números primos.

class NumerosPrimos:
    def __init__(self, limite):
        self.limite = limite
    
    # Método para verificar si un número es primo
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Método para calcular todos los números primos hasta el límite dado
    def calcular_primos(self):
        return [i for i in range(2, self.limite + 1) if self.es_primo(i)]
    
# Uso de los estilos
num = int(input("Ingrese un número: "))
print("Orientado a Objetos:", NumerosPrimos(num).calcular_primos())