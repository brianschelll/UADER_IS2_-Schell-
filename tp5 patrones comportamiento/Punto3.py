class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, emitted_id):
        print(f"\nEmitiendo ID: {emitted_id}")
        for observer in self.observers:
            observer.update(emitted_id)


class ObservadorA123:
    def update(self, emitted_id):
        if emitted_id == "A123":
            print("Observador A123: ¡Coincidencia detectada!")


class ObservadorB456:
    def update(self, emitted_id):
        if emitted_id == "B456":
            print("Observador B456: ¡Coincidencia detectada!")


class ObservadorC789:
    def update(self, emitted_id):
        if emitted_id == "C789":
            print("Observador C789: ¡Coincidencia detectada!")


class ObservadorX999:
    def update(self, emitted_id):
        if emitted_id == "X999":
            print("Observador X999: ¡Coincidencia detectada!")


# Sujeto
subject = Subject()

# Observadores
obs1 = ObservadorA123()
obs2 = ObservadorB456()
obs3 = ObservadorC789()
obs4 = ObservadorX999()

# Observadores
subject.attach(obs1)
subject.attach(obs2)
subject.attach(obs3)
subject.attach(obs4)

# 8 IDs (al menos 4 coinciden)
emitted_ids = ["Z111", "A123", "B456", "T000", "C789", "X999", "L111", "Y222"]

for id_emitted in emitted_ids:
    subject.notify(id_emitted)
