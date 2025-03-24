#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

# Definir los límites del rango (1 a 500)
lower = 1
upper = 500

# Imprimir el mensaje indicando el rango
print("Prime numbers between", lower, "and", upper, "are:")

# Iterar sobre el rango de números
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       # Comprobar si el número es divisible por algún número menor que él
       for i in range(2, num):
           # Si el número es divisible por algún otro número, no es primo
           if (num % i) == 0:
               break
       else:
           # Si no es divisible por ningún número, es primo y se imprime
           print(num)
