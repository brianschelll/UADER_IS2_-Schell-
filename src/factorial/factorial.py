#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

# Verificar si se ingresó un número como argumento
if len(sys.argv) > 1:
    num = int(sys.argv[1])  # Toma el argumento de la línea de comandos
else:
    num = int(input("Ingrese un número para calcular su factorial: "))  # Solicita el número manualmente

print("Factorial ", num, "! es ", factorial(num))

