#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * Calcula el factorial de un número o un rango de números                 *
# * Dr.P.E.Colla (c) 2022 - Modificado en 2025                              *
# * Creative Commons                                                        *
# *-------------------------------------------------------------------------*

import sys

def factorial(num): 
    
    if num < 0: 
        return None  
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 


if len(sys.argv) < 2:
    entrada = input("Ingrese un número o un rango (ej. 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]


desde, hasta = None, None

if "-" in entrada:
    partes = entrada.split("-")
    
    if entrada.startswith("-") and partes[1].isdigit():
        
        desde = 1
        hasta = int(partes[1])
    
    elif entrada.endswith("-") and partes[0].isdigit():
        
        desde = int(partes[0])
        hasta = 60
    
    elif partes[0].isdigit() and partes[1].isdigit():
        
        desde = int(partes[0])
        hasta = int(partes[1])

else:
    
    desde = hasta = int(entrada)


if desde is not None and desde < 0:
    print(f"El factorial de {desde} no está definido.")
    sys.exit(1)
if hasta is not None and hasta < 0:
    print(f"El factorial de {hasta} no está definido.")
    sys.exit(1)


for num in range(desde, hasta + 1):
    resultado = factorial(num)
    print(f"Factorial de {num}: {resultado}")
