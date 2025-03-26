#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial_OOP.py                                                        *
# * Calcula el factorial de un número o un rango de números usando OOP      *
# * Implementa la lógica en la clase Factorial                              *
# *-------------------------------------------------------------------------*

import sys

class Factorial:
    """Clase para calcular factoriales en un rango de números"""
    
    def __init__(self, min_value=1, max_value=1):
        """Inicializa los valores mínimos y máximos del rango"""
        self.min_value = min_value
        self.max_value = max_value

    def calcular(self, num):
        """Calcula el factorial de un número entero no negativo"""
        if num < 0:
            return None  # No se define factorial para números negativos
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self):
        """Calcula y muestra el factorial de los números en el rango"""
        for num in range(self.min_value, self.max_value + 1):
            resultado = self.calcular(num)
            print(f"Factorial de {num}: {resultado}")

# Procesar argumentos de entrada
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o un rango (ej. 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]

# Determinar el rango de cálculo
min_value, max_value = None, None

if "-" in entrada:
    partes = entrada.split("-")
    
    if entrada.startswith("-") and partes[1].isdigit():
        min_value, max_value = 1, int(partes[1])
    elif entrada.endswith("-") and partes[0].isdigit():
        min_value, max_value = int(partes[0]), 60
    elif partes[0].isdigit() and partes[1].isdigit():
        min_value, max_value = int(partes[0]), int(partes[1])
else:
    min_value = max_value = int(entrada)

# Validación de números negativos
if min_value is not None and min_value < 0:
    print(f"El factorial de {min_value} no está definido.")
    sys.exit(1)
if max_value is not None and max_value < 0:
    print(f"El factorial de {max_value} no está definido.")
    sys.exit(1)

# Instanciar la clase y ejecutar el cálculo
fact = Factorial(min_value, max_value)
fact.run()
