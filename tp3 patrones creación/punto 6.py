import copy

# Clase prototipo
class AvionPrototipo:
    def __init__(self, modelo, capacidad):
        self.modelo = modelo
        self.capacidad = capacidad

    def clonar(self):
        return copy.deepcopy(self)

    def mostrar_info(self):
        print(f"✈️ Modelo: {self.modelo} - Capacidad: {self.capacidad} pasajeros")

# Uso del patrón Prototype
if __name__ == "__main__":
    # Creamos el prototipo original
    avion_original = AvionPrototipo("Boeing 747", 400)
    print("Avión original:")
    avion_original.mostrar_info()

    # Creamos una copia (clon 1)
    clon1 = avion_original.clonar()
    clon1.modelo = "Boeing 747 Clonado"
    print("\nPrimer clon:")
    clon1.mostrar_info()

    # Creamos una copia del clon (clon 2)
    clon2 = clon1.clonar()
    clon2.modelo = "Boeing 747 Clonado 2 veces"
    print("\nSegundo clon (copiado del primero):")
    clon2.mostrar_info()
