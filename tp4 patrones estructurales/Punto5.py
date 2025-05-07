class Pieza:
    def __init__(self, tipo, color):
        self.tipo = tipo         
        self.color = color       

    def mostrar(self, posicion):
        print(f"Pieza: {self.color} {self.tipo} en posición {posicion}")


class FabricaDePiezas:
    _piezas = {}

    @classmethod
    def obtener_pieza(cls, tipo, color):
        clave = (tipo, color)
        if clave not in cls._piezas:
            cls._piezas[clave] = Pieza(tipo, color)
        return cls._piezas[clave]


# Uso del Flyweight
posiciones = [
    ("peon", "blanco", "A2"),
    ("peon", "blanco", "B2"),
    ("peon", "blanco", "C2"),
    ("torre", "negro", "A8"),
    ("torre", "negro", "H8")
]

for tipo, color, posicion in posiciones:
    pieza = FabricaDePiezas.obtener_pieza(tipo, color)
    pieza.mostrar(posicion)

# Ver cuántas instancias únicas se crearon
print(f"\nTotal de objetos únicos de piezas creados: {len(FabricaDePiezas._piezas)}")
