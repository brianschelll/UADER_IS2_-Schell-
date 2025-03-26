#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número o un rango de números                 *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Modificado por: [Brian]                                                 *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

import sys

def factorial(num): 
    if num < 0: 
        print(f"Factorial de {num} no existe")
        return None
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

def calcular_factoriales(desde, hasta):
    for num in range(desde, hasta + 1):
        print(f"Factorial {num}! es {factorial(num)}")

# Obtener el argumento o solicitar entrada manual
if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    entrada = input("Ingrese un número o un rango (ej. 4-8): ")

# Verificar si es un rango o un solo número
if '-' in entrada:
    try:
        desde, hasta = map(int, entrada.split('-'))
        if desde > hasta:
            print("Error: el primer número debe ser menor o igual al segundo.")
        else:
            calcular_factoriales(desde, hasta)
    except ValueError:
        print("Formato inválido. Use un solo número o un rango en formato desde-hasta.")
else:
    try:
        num = int(entrada)
        print(f"Factorial {num}! es {factorial(num)}")
    except ValueError:
        print("Ingrese un número válido.")


