class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(f"Escaneando... Estación: {self.stations[self.pos]} {self.name}")


class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate


class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

        # Memorias (pueden ser AM o FM)
        self.memorias = {
            "M1": ("AM", "1380"),
            "M2": ("FM", "89.1"),
            "M3": ("AM", "1510"),
            "M4": ("FM", "103.9")
        }

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()
        self.scan_memorias()

    def scan_memorias(self):
        print("Escaneando memorias:")
        for etiqueta, (banda, frecuencia) in self.memorias.items():
            print(f" - {etiqueta}: {banda} {frecuencia}")


if __name__ == "__main__":
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2

    for action in actions:
        action()
