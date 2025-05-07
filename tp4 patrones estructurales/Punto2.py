from abc import ABC, abstractmethod

# Implementador
class TrenLaminador(ABC):
    @abstractmethod
    def laminar(self):
        pass

# Implementaciones concretas
class TrenLaminador5mts(TrenLaminador):
    def laminar(self):
        print("Laminando una lámina de acero de 5 metros.")

class TrenLaminador10mts(TrenLaminador):
    def laminar(self):
        print("Laminando una lámina de acero de 10 metros.")

# Abstracción
class LaminaAcero:
    def __init__(self, tren: TrenLaminador):
        self.tren = tren
        self.espesor = 0.5  # pulgadas
        self.ancho = 1.5    # metros

    def producir(self):
        print(f"Produciendo lámina de {self.espesor}'' de espesor y {self.ancho}m de ancho.")
        self.tren.laminar()

# Ejecución principal
if __name__ == "__main__":
    # Crear trenes laminadores
    tren5 = TrenLaminador5mts()
    tren10 = TrenLaminador10mts()

    # Crear láminas asignadas a cada tren
    lamina1 = LaminaAcero(tren5)
    lamina2 = LaminaAcero(tren10)

    # Producir láminas
    lamina1.producir()
    print()
    lamina2.producir()
