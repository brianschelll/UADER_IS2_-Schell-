# Producto final: el avión con sus partes
class Avion:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar_partes(self):
        print("✈️ Avión construido con las siguientes partes:")
        for parte in self.partes:
            print(f" - {parte}")

# Builder abstracto
class AvionBuilder:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self):
        pass

    def construir_turbinas(self):
        pass

    def construir_alas(self):
        pass

    def construir_tren_aterrizaje(self):
        pass

    def obtener_avion(self):
        return self.avion

# Builder concreto
class AvionComercialBuilder(AvionBuilder):
    def construir_body(self):
        self.avion.agregar_parte("Cuerpo del avión comercial")

    def construir_turbinas(self):
        self.avion.agregar_parte("Turbina izquierda")
        self.avion.agregar_parte("Turbina derecha")

    def construir_alas(self):
        self.avion.agregar_parte("Ala izquierda")
        self.avion.agregar_parte("Ala derecha")

    def construir_tren_aterrizaje(self):
        self.avion.agregar_parte("Tren de aterrizaje triple")

# Director
class DirectorAvion:
    def __init__(self, builder):
        self.builder = builder

    def construir_avion(self):
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren_aterrizaje()
        return self.builder.obtener_avion()

# Ejecución
if __name__ == "__main__":
    builder = AvionComercialBuilder()
    director = DirectorAvion(builder)
    avion = director.construir_avion()
    avion.mostrar_partes()
