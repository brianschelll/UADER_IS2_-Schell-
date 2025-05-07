from abc import ABC, abstractmethod

# Clase abstracta base
class Factura(ABC):
    def __init__(self, importe):
        self.importe = importe

    @abstractmethod
    def mostrar_factura(self):
        pass

# Subclases para cada condición impositiva
class FacturaIVAResponsable(Factura):
    def mostrar_factura(self):
        print(f"Factura A - IVA Responsable. Importe: ${self.importe:.2f}")

class FacturaIVANoInscripto(Factura):
    def mostrar_factura(self):
        print(f"Factura C - IVA No Inscripto. Importe: ${self.importe:.2f}")

class FacturaIVAExento(Factura):
    def mostrar_factura(self):
        print(f"Factura E - IVA Exento. Importe: ${self.importe:.2f}")

# Factory para generar la factura correcta
class FacturaFactory:
    @staticmethod
    def crear_factura(condicion_impositiva, importe):
        condicion = condicion_impositiva.lower()
        if condicion == "iva responsable":
            return FacturaIVAResponsable(importe)
        elif condicion == "iva no inscripto":
            return FacturaIVANoInscripto(importe)
        elif condicion == "iva exento":
            return FacturaIVAExento(importe)
        else:
            raise ValueError("Condición impositiva no válida. Use: IVA Responsable, IVA No Inscripto, IVA Exento.")

# Uso desde consola
if __name__ == "__main__":
    try:
        importe = float(input("Ingrese el importe de la factura: "))
        condicion = input("Ingrese la condición impositiva (IVA Responsable / IVA No Inscripto / IVA Exento): ")

        factura = FacturaFactory.crear_factura(condicion, importe)
        factura.mostrar_factura()

    except ValueError as e:
        print("Error:", e)
