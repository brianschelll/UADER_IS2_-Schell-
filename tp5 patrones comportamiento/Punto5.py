class Originator:
    def __init__(self, text):
        self.text = text

    def set_text(self, text):
        self.text = text

    def create_memento(self):
        return Memento(self.text)

    def restore_memento(self, memento):
        self.text = memento.get_state()

    def __str__(self):
        return self.text


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self):
        self._mementos = []

    def save(self, memento):
        if len(self._mementos) == 4:
            self._mementos.pop(0)
        self._mementos.append(memento)

    def undo(self, index):
        max_index = len(self._mementos) - 2
        if 0 <= index <= max_index:
            pos = -(index + 2)
            return self._mementos[pos]
        return None


if __name__ == "__main__":
    editor = Originator("Texto inicial")
    caretaker = Caretaker()
    caretaker.save(editor.create_memento())

    print("Editor iniciado. Escribí texto para guardar, 'undo <n>' para deshacer (0–3), 'mostrar' para ver texto, 'salir' para terminar.\n")

    while True:
        entrada = input("> ")

        if entrada.lower() == "salir":
            print("Hasta luego.")
            break
        elif entrada.lower() == "mostrar":
            print(f"Texto actual: {editor}")
        elif entrada.startswith("undo"):
            try:
                _, n = entrada.split()
                index = int(n)
                memento = caretaker.undo(index)
                if memento:
                    editor.restore_memento(memento)
                    print(f"Restaurado a estado anterior (undo {index}): {editor}")
                else:
                    print(" No hay un estado disponible en esa posición.")
            except:
                print(" Usá el formato: undo 0 (o 1, 2, 3)")
        else:
            editor.set_text(entrada)
            caretaker.save(editor.create_memento())
            print(" Texto guardado.")

