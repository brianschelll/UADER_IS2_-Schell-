class CalculadoraImpuestos:
    """
    Clase Singleton para calcular impuestos sobre una base imponible.
    Aplica IVA (21%), IIBB (5%) y Contribuciones municipales (1.2%).
    """
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instancia

    def calcular_total_impuestos(self, base):
        """
        Calcula el total de impuestos sobre la base imponible.
        :param base: importe base imponible (float o int)
        :return: tuple con (total, iva, iibb, contribuciones)
        """
        if base < 0:
            raise ValueError("La base imponible no puede ser negativa")

        iva = base * 0.21
        iibb = base * 0.05
        contribuciones = base * 0.012
        total = iva + iibb + contribuciones
        return total, iva, iibb, contribuciones


# Ejecución principal con entrada de usuario
if __name__ == "__main__":
    try:
        base = float(input("Ingrese el importe base imponible: "))
        calculadora = CalculadoraImpuestos()
        total, iva, iibb, contribuciones = calculadora.calcular_total_impuestos(base)

        print(f"\nDetalle de impuestos para una base de ${base:.2f}:")
        print(f"- IVA (21%): ${iva:.2f}")
        print(f"- IIBB (5%): ${iibb:.2f}")
        print(f"- Contribuciones municipales (1.2%): ${contribuciones:.2f}")
        print(f"=> Total impuestos: ${total:.2f}")

    except ValueError as e:
        print("Error:", e)
