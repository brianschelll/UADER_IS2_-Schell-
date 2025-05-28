"""
getJason.py - Programa para extraer valores de claves específicas en archivos JSON
Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.

Versión: 1.1
"""

import json
import sys
import os

# ---------------------------
# Código viejo (procedural)
# ---------------------------
"""
def get_value_old(jsonfile, jsonkey='token1'):
    '''
    Método original procedimental para obtener el valor de una clave en un JSON.
    Parámetros:
      - jsonfile: ruta al archivo JSON
      - jsonkey: clave a buscar (por defecto 'token1')
    Retorna:
      - Valor asociado a la clave o mensaje de error.
    '''
    try:
        with open(jsonfile, 'r', encoding='utf-8') as myfile:
            data = myfile.read()
        obj = json.loads(data)
        if jsonkey in obj:
            return obj[jsonkey]
        else:
            return f"[ERROR] La clave '{jsonkey}' no existe en el archivo JSON."
    except FileNotFoundError:
        return f"[ERROR] El archivo '{jsonfile}' no fue encontrado."
    except json.JSONDecodeError:
        return "[ERROR] El archivo no contiene un JSON válido."
"""

# ---------------------------
# Nueva abstracción / interfaz
# ---------------------------
class JsonReaderInterface:
    '''
    Interfaz base para clases lectoras de JSON.
    Define el método get_value que debe implementarse.
    '''
    def get_value(self) -> str:
        raise NotImplementedError("Método no implementado.")

# ---------------------------
# Nueva implementación Singleton
# ---------------------------
class JsonReaderSingleton(JsonReaderInterface):
    '''
    Implementación Singleton para lectura de JSON.
    Asegura que sólo una instancia del lector exista durante la ejecución.
    '''
    _instance = None

    def __new__(cls, filepath: str, key: str = 'token1'):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, filepath: str, key: str = 'token1'):
        if self._initialized:
            return
        self.filepath = filepath
        self.key = key
        self.data = None
        self._initialized = True

    def load_file(self):
        '''
        Carga y decodifica el archivo JSON.
        Lanza FileNotFoundError si no encuentra el archivo.
        '''
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"[ERROR] Archivo no encontrado: '{self.filepath}'")
        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get_value(self):
        '''
        Obtiene el valor asociado a la clave buscada en el JSON.
        Lanza KeyError si la clave no existe.
        '''
        if self.data is None:
            self.load_file()
        if self.key in self.data:
            return self.data[self.key]
        raise KeyError(f"[ERROR] Clave inexistente: '{self.key}'")

# ---------------------------
# Fábrica para elegir implementación
# ---------------------------
def create_json_reader(filepath: str, key: str = 'token1') -> JsonReaderInterface:
    '''
    Fábrica para crear la instancia del lector JSON.
    Actualmente retorna la implementación Singleton.
    '''
    return JsonReaderSingleton(filepath, key)

# ---------------------------
# Función para mostrar ayuda
# ---------------------------
def print_help():
    '''
    Muestra el uso y opciones del programa.
    '''
    print("Uso: python getJason.py <archivo_json> [clave]")
    print("  <archivo_json>: ruta al archivo JSON")
    print("  [clave]: clave a buscar (opcional, por defecto: token1)")
    print("  -v: muestra la versión del programa")
    print("  -h o --help: muestra esta ayuda")

# ---------------------------
# Función principal con validación robusta de argumentos (punto f)
# ---------------------------
def main():
    '''
    Controla la ejecución desde línea de comandos,
    validando argumentos y manejando errores de forma controlada.
    '''
    args = sys.argv[1:]

    # Validar argumentos especiales
    if len(args) == 1 and args[0] in ('-h', '--help'):
        print_help()
        return

    if len(args) == 1 and args[0] == '-v':
        print("Versión 1.1")
        return

    # Validar cantidad de argumentos (archivo + clave opcional)
    if len(args) == 0:
        print("[ERROR] Falta el archivo JSON.\n")
        print_help()
        return

    if len(args) > 2:
        print("[ERROR] Demasiados argumentos.\n")
        print_help()
        return

    jsonfile = args[0]
    jsonkey = args[1] if len(args) == 2 else 'token1'

    # Validar extensión del archivo
    if not jsonfile.lower().endswith('.json'):
        print("[ERROR] El archivo debe tener extensión '.json'.")
        return

    # Validar clave no vacía
    if not jsonkey.strip():
        print("[ERROR] La clave no puede estar vacía.")
        return

    try:
        reader = create_json_reader(jsonfile, jsonkey)
        print(reader.get_value())
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
        print(e)
    except Exception:
        print("[ERROR] Ocurrió un error inesperado durante la ejecución.")

if __name__ == "__main__":
    main()
