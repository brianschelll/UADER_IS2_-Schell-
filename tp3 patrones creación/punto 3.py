from abc import ABC, abstractmethod

# Clase abstracta base para las estrategias de entrega
class MetodoEntrega(ABC):
    @abstractmethod
    def entregar(self):
        pass

# Implementaciones concretas de los métodos de entrega
class EntregaMostrador(MetodoEntrega):
    def entregar(self):
        print("La hamburguesa será entregada en el mostrador.")

class RetiroCliente(MetodoEntrega):
    def entregar(self):
        print("El cliente retirará la hamburguesa.")

class Delivery(MetodoEntrega):
    def entregar(self):
        print("La hamburguesa será enviada por delivery.")

# Clase Hamburguesa que usa una estrategia de entrega
class Hamburguesa:
    def __init__(self, metodo_entrega: MetodoEntrega):
        self.metodo_entrega = metodo_entrega

    def entregar(self):
        self.metodo_entrega.entregar()

# Factory para crear hamburguesas con el método de entrega elegido
class HamburguesaFactory:
    @staticmethod
    def crear_hamburguesa(tipo):
        if tipo == "mostrador":
            return Hamburguesa(EntregaMostrador())
        elif tipo == "retiro":
            return Hamburguesa(RetiroCliente())
        elif tipo == "delivery":
            return Hamburguesa(Delivery())
        else:
            raise ValueError("Tipo de entrega no válido. Use: mostrador, retiro, delivery.")

# Ejecución desde consola
if __name__ == "__main__":
    tipo = input("Seleccione el tipo de entrega (mostrador / retiro / delivery): ").lower()
    try:
        hamburguesa = HamburguesaFactory.crear_hamburguesa(tipo)
        hamburguesa.entregar()
    except ValueError as e:
        print("Error:", e)
