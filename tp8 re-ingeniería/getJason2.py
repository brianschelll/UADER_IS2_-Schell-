"""
get_jason1.py - Sistema de gestión de pagos automático con lectura de claves desde JSON.
Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.

Versión: 1.2
"""

import json
import sys
import os

# ---------------------------
# Código viejo (procedural)
# ---------------------------
# def get_value_old(jsonfile, jsonkey='token1'):
#     """
#     Método original procedimental para obtener el valor de una clave en un JSON.
#     Parámetros:
#       - jsonfile: ruta al archivo JSON
#       - jsonkey: clave a buscar (por defecto 'token1')
#     Retorna:
#       - Valor asociado a la clave o mensaje de error.
#     """
#     try:
#         with open(jsonfile, 'r', encoding='utf-8') as myfile:
#             data = myfile.read()
#         obj = json.loads(data)
#         if jsonkey in obj:
#             return obj[jsonkey]
#         else:
#             return f"[ERROR] La clave '{jsonkey}' no existe en el archivo JSON."
#     except FileNotFoundError:
#         return f"[ERROR] El archivo '{jsonfile}' no fue encontrado."
#     except json.JSONDecodeError:
#         return "[ERROR] El archivo no contiene un JSON válido."


class JsonReaderInterface:
    """Interfaz para la lectura de valores desde un archivo JSON."""

    def get_value(self) -> str:
        """Obtiene el valor asociado a una clave en el JSON."""
        raise NotImplementedError("Método no implementado.")


class JsonReaderSingleton(JsonReaderInterface):
    """Singleton que asegura una única instancia para leer un JSON."""

    _instance = None
    _initialized = False  # Se define aquí para evitar error de acceso antes de asignar

    def __new__(cls, filepath: str, key: str = 'token1'):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, filepath: str, key: str = 'token1'):
        """Inicializa el lector con ruta y clave a buscar."""
        if self._initialized:
            return
        self.filepath = filepath
        self.key = key
        self.data = None
        self._initialized = True

    def load_file(self):
        """Carga el contenido del archivo JSON."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"[ERROR] Archivo no encontrado: '{self.filepath}'")
        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get_value(self):
        """Retorna el valor asociado a la clave definida."""
        if self.data is None:
            self.load_file()
        if self.key in self.data:
            return self.data[self.key]
        raise KeyError(f"[ERROR] Clave inexistente: '{self.key}'")


def create_json_reader(filepath: str, key: str = 'token1') -> JsonReaderInterface:
    """Fábrica para crear instancia singleton del lector JSON."""
    return JsonReaderSingleton(filepath, key)


class CuentaPago:
    """Modelo de una cuenta para realizar pagos."""

    def __init__(self, nombre_token: str, clave: str, saldo_inicial: float):
        """
        Inicializa la cuenta con token, clave y saldo.

        Args:
            nombre_token (str): Nombre identificador del token.
            clave (str): Clave asociada al token.
            saldo_inicial (float): Saldo disponible inicial.
        """
        self.nombre_token = nombre_token
        self.clave = clave
        self.saldo = saldo_inicial

    def puede_pagar(self, monto: float) -> bool:
        """Indica si la cuenta tiene saldo suficiente para el pago."""
        return self.saldo >= monto

    def realizar_pago(self, monto: float) -> bool:
        """
        Realiza el pago descontando el monto si hay saldo suficiente.

        Args:
            monto (float): Monto a pagar.

        Returns:
            bool: True si el pago fue realizado, False si no hay saldo suficiente.
        """
        if self.puede_pagar(monto):
            self.saldo -= monto
            return True
        return False


class ManejadorPago:
    """Manejador que administra cuentas y procesa pagos en orden rotativo."""

    def __init__(self):
        """Inicializa la lista de cuentas y el índice de turno."""
        self.cuentas = []
        self.turno = 0

    def agregar_cuenta(self, cuenta: CuentaPago):
        """Agrega una cuenta a la lista de manejo."""
        self.cuentas.append(cuenta)

    def procesar_pago(self, numero_pedido: int, monto: float, registro):
        """
        Procesa un pago buscando una cuenta con saldo suficiente.

        Args:
            numero_pedido (int): Número identificador del pedido.
            monto (float): Monto a pagar.
            registro (RegistroPagos): Objeto para registrar pagos realizados.
        """
        for intento in range(len(self.cuentas)):
            idx = (self.turno + intento) % len(self.cuentas)
            cuenta = self.cuentas[idx]
            if cuenta.puede_pagar(monto):
                cuenta.realizar_pago(monto)
                self.turno = idx + 1
                registro.agregar_pago(numero_pedido, cuenta.nombre_token, monto)
                print(f"Pedido #{numero_pedido} pagado con {cuenta.nombre_token}")
                return
        print(f"[ERROR] Pedido #{numero_pedido} no procesado: saldo insuficiente.")


class RegistroPagos:
    """Registro persistente de pagos realizados."""

    def __init__(self, archivo: str = 'pagos.json'):
        """
        Inicializa el registro y carga pagos existentes si hay.

        Args:
            archivo (str): Nombre del archivo JSON donde se guardan los pagos.
        """
        self.archivo = archivo
        self.pagos = self.cargar_pagos()

    def cargar_pagos(self) -> list:
        """Carga la lista de pagos desde el archivo JSON, si existe."""
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def guardar_pagos(self):
        """Guarda la lista de pagos actual en el archivo JSON."""
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(self.pagos, f, indent=2)

    def agregar_pago(self, numero_pedido: int, token: str, monto: float):
        """
        Agrega un nuevo pago al registro y guarda en archivo.

        Args:
            numero_pedido (int): Número identificador del pedido.
            token (str): Token usado para el pago.
            monto (float): Monto pagado.
        """
        self.pagos.append({
            'pedido': numero_pedido,
            'token': token,
            'monto': monto
        })
        self.guardar_pagos()

    def listar_pagos(self):
        """Imprime por pantalla el listado de pagos realizados."""
        print("\nListado de pagos realizados:")
        if not self.pagos:
            print("No hay pagos registrados.")
            return
        for pago in self.pagos:
            print(f"Pedido #{pago['pedido']}: Token={pago['token']}, Monto=${pago['monto']}")


def print_help():
    """Imprime el mensaje de ayuda del programa."""
    print("Uso:")
    print("  python get_jason1.py pagar       # Realiza pagos automáticos de $500")
    print("  python get_jason1.py listar      # Muestra pagos realizados")
    print("  python get_jason1.py -v          # Muestra la versión")
    print("  python get_jason1.py -h|--help   # Muestra esta ayuda")


def main():
    """Función principal que procesa argumentos y ejecuta comandos."""
    args = sys.argv[1:]

    if not args or args[0] in ('-h', '--help'):
        print_help()
        return

    if args[0] == '-v':
        print("Versión 1.2")
        return

    if args[0] not in ('pagar', 'listar'):
        print("[ERROR] Comando inválido.\n")
        print_help()
        return

    json_file = 'sitedata.json'
    reader1 = create_json_reader(json_file, 'token1')
    reader2 = create_json_reader(json_file, 'token2')

    cuenta1 = CuentaPago('token1', reader1.get_value(), 1000)
    cuenta2 = CuentaPago('token2', reader2.get_value(), 2000)

    manejador = ManejadorPago()
    manejador.agregar_cuenta(cuenta1)
    manejador.agregar_cuenta(cuenta2)

    registro = RegistroPagos()

    if args[0] == 'pagar':
        for i in range(1, 6):  # Simula 5 pagos de $500
            manejador.procesar_pago(i, 500, registro)

    elif args[0] == 'listar':
        registro.listar_pagos()


if __name__ == "__main__":
    main()
