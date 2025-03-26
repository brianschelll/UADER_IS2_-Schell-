#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * Calcula el factorial de un número o un rango de números                 *
# * Dr.P.E.Colla (c) 2022 - Modificado en 2025                              *
# * Creative Commons                                                        *
# *-------------------------------------------------------------------------*

import sys

def factorial(num): 
    """Calcula el factorial de un número entero no negativo"""
    if num < 0: 
        return None  # Retorna None si el número es negativo
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

# Verificar si hay argumentos
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o un rango (ej. 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]

# Determinar el rango de cálculo
desde, hasta = None, None

if "-" in entrada:
    partes = entrada.split("-")
    
    if entrada.startswith("-") and partes[1].isdigit():
        # Caso "-hasta": calcula desde 1 hasta el número dado
        desde = 1
        hasta = int(partes[1])
    
    elif entrada.endswith("-") and partes[0].isdigit():
        # Caso "desde-": calcula desde el número dado hasta 60
        desde = int(partes[0])
        hasta = 60
    
    elif partes[0].isdigit() and partes[1].isdigit():
        # Caso "desde-hasta": calcula entre los dos números dados
        desde = int(partes[0])
        hasta = int(partes[1])

else:
    # Caso de un solo número
    desde = hasta = int(entrada)

# Validación de números negativos
if desde is not None and desde < 0:
    print(f"El factorial de {desde} no está definido.")
    sys.exit(1)
if hasta is not None and hasta < 0:
    print(f"El factorial de {hasta} no está definido.")
    sys.exit(1)

# Cálculo de factoriales en el rango determinado
for num in range(desde, hasta + 1):
    resultado = factorial(num)
    print(f"Factorial de {num}: {resultado}")
