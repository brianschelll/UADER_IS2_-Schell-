class CalculadoraFactorial:
    """
    Clase Singleton para calcular el factorial de un número entero.
    Garantiza que todas las clases que la usen compartan la misma instancia.
    """
    _instancia = None  # Atributo de clase para mantener la instancia única

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(CalculadoraFactorial, cls).__new__(cls)
        return cls._instancia

    def calcular_factorial(self, n):
        """
        Calcula el factorial del número entero n.
        :param n: número entero no negativo
        :return: factorial de n
        """
        if n < 0:
            raise ValueError("El número debe ser mayor o igual a 0")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado


# Programa principal con entrada por teclado
if __name__ == "__main__":
    try:
        numero = int(input("Ingrese un número entero para calcular su factorial: "))
        calculadora = CalculadoraFactorial()
        resultado = calculadora.calcular_factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
    except ValueError as e:
        print("Error:", e)


