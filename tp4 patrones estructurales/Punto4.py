# tp4_decorator.py

from abc import ABC, abstractmethod

# Componente base
class Numero(ABC):
    @abstractmethod
    def obtener_valor(self):
        pass

# Componente concreto
class NumeroConcreto(Numero):
    def __init__(self, valor):
        self.valor = valor

    def obtener_valor(self):
        return self.valor

# Decorador abstracto
class OperacionDecorator(Numero):
    def __init__(self, componente: Numero):
        self.componente = componente

# Decoradores concretos
class SumarDos(OperacionDecorator):
    def obtener_valor(self):
        return self.componente.obtener_valor() + 2

class MultiplicarPorDos(OperacionDecorator):
    def obtener_valor(self):
        return self.componente.obtener_valor() * 2

class DividirPorTres(OperacionDecorator):
    def obtener_valor(self):
        return self.componente.obtener_valor() / 3

# Uso
numero_base = NumeroConcreto(6)
print("Valor original:", numero_base.obtener_valor())

# Aplicando decoradores anidados
numero_modificado = DividirPorTres(MultiplicarPorDos(SumarDos(numero_base)))
print("Valor con operaciones (sumar 2, multiplicar por 2, dividir por 3):", numero_modificado.obtener_valor())
