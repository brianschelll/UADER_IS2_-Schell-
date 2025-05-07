from abc import ABC, abstractmethod

# Interfaces de producto
class Asiento(ABC):
    @abstractmethod
    def tipo(self):
        pass

class Motor(ABC):
    @abstractmethod
    def potencia(self):
        pass

# Productos concretos: comerciales
class AsientoComercial(Asiento):
    def tipo(self):
        return "Asiento de clase turista"

class MotorComercial(Motor):
    def potencia(self):
        return "Motor de 2 turbinas estándar"

# Productos concretos: militares
class AsientoMilitar(Asiento):
    def tipo(self):
        return "Asiento eyectable"

class MotorMilitar(Motor):
    def potencia(self):
        return "Motor con postcombustión"

# Abstract Factory
class FabricaAvion(ABC):
    @abstractmethod
    def crear_asiento(self):
        pass

    @abstractmethod
    def crear_motor(self):
        pass

# Fábricas concretas
class FabricaAvionComercial(FabricaAvion):
    def crear_asiento(self):
        return AsientoComercial()

    def crear_motor(self):
        return MotorComercial()

class FabricaAvionMilitar(FabricaAvion):
    def crear_asiento(self):
        return AsientoMilitar()

    def crear_motor(self):
        return MotorMilitar()

# Cliente
class EnsambladorAvion:
    def __init__(self, fabrica: FabricaAvion):
        self.asiento = fabrica.crear_asiento()
        self.motor = fabrica.crear_motor()

    def mostrar_componentes(self):
        print("🛠️ Componentes del avión:")
        print(f"- Asiento: {self.asiento.tipo()}")
        print(f"- Motor: {self.motor.potencia()}")

# Uso desde consola
if __name__ == "__main__":
    tipo = input("¿Qué tipo de avión desea ensamblar? (comercial / militar): ").lower()

    if tipo == "comercial":
        fabrica = FabricaAvionComercial()
    elif tipo == "militar":
        fabrica = FabricaAvionMilitar()
    else:
        print("Tipo no válido.")
        exit()

    ensamblador = EnsambladorAvion(fabrica)
    ensamblador.mostrar_componentes()
