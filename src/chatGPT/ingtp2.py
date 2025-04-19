# Autor: Brian Schell
# Trabajo Práctico 2 - Ingeniería de Software II

# === Chat con Gemini ===
# Este script permite interactuar con Gemini (modelo de lenguaje de Google)
# desde la terminal mediante una interfaz de consola.
# Está pensado para ser multiplataforma (Windows y Unix)

import google.generativeai as genai

# Importar readline según el sistema operativo
# Esto permite que se active el historial de entrada (↑ ↓)
try:
    import readline  # Unix/macOS
except ImportError:
    import pyreadline as readline  # type: ignore # Windows (pyreadline3)
readline  # Mantener readline como usado para evitar warning de pylint

# Configuración de la API Key
genai.configure(api_key="AIzaSyCsJDmvib4-Xr3z3hdxJVoodO4xeProL70")

# Inicialización del modelo Gemini 1.5 Flash
model = genai.GenerativeModel("gemini-2.0-flash")

def main():
    print("=== Chat con Gemini ===\n")

    # Bucle principal de interacción con el usuario
    while True:
        try:
            try:
                # Leer entrada del usuario
                user_input = input("Tu consulta ('salir' para terminar): ")

                # Opción para salir
                if user_input.lower() == "salir":
                    print("¡Hasta luego!")
                    break

            except Exception as e:
                # Error al ingresar texto
                print(f"Error al ingresar la consulta: {e}")
                continue

            try:
                # Validar entrada vacía
                if not user_input.strip():
                    print("La consulta no puede estar vacía.")
                    continue

                print(f"You: {user_input}")

            except Exception as e:
                # Error al procesar la consulta
                print(f"Error al procesar la consulta: {e}")
                continue

            try:
                # Llamada al modelo Gemini
                respuesta = model.generate_content(user_input)

                # Mostrar respuesta del modelo
                print("Gemini:", respuesta.text)

            except Exception as e:
                # Error al generar respuesta con el modelo
                print(f"Error al invocar a Gemini: {e}")
                continue

        except Exception as e:
            # Error inesperado en el ciclo
            print(f"Error inesperado: {e}")

# Punto de entrada del script
if __name__ == "__main__":
    main()
