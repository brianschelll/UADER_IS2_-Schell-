from abc import ABC, abstractmethod

# Componente base
class Componente(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar(self, nivel=0):
        pass

# Hoja: Pieza individual
class Pieza(Componente):
    def mostrar(self, nivel=0):
        print("  " * nivel + f"Pieza: {self.nombre}")

# Compuesto: Puede contener piezas o subconjuntos
class SubConjunto(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Subconjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)

# Producto principal
producto_principal = SubConjunto("Producto Principal")

# 3 subconjuntos con 4 piezas cada uno
for i in range(1, 4):
    subconjunto = SubConjunto(f"Subconjunto {i}")
    for j in range(1, 5):
        pieza = Pieza(f"Pieza {i}.{j}")
        subconjunto.agregar(pieza)
    producto_principal.agregar(subconjunto)

# Configuración inicial
print("Configuración inicial del ensamblado:")
producto_principal.mostrar()

# Agregar subconjunto opcional adicional
subconjunto_opcional = SubConjunto("Subconjunto Opcional")
for j in range(1, 5):
    pieza = Pieza(f"Pieza Opcional.{j}")
    subconjunto_opcional.agregar(pieza)

producto_principal.agregar(subconjunto_opcional)

# Mostrar configuración final
print("\nConfiguración final del ensamblado con subconjunto opcional:")
producto_principal.mostrar()
