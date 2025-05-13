class StringContainer:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return ForwardIterator(self.text)

    def reverse_iterator(self):
        return ReverseIterator(self.text)


class ForwardIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.text):
            result = self.text[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


class ReverseIterator:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            result = self.text[self.index]
            self.index -= 1
            return result
        else:
            raise StopIteration


while True:
    user_input = input("\nIngresá una cadena (o escribí 'salir' para terminar): ")
    if user_input.lower() == "salir":
        print("Hasta luego.")
        break

    container = StringContainer(user_input)

    print("Recorrido directo:")
    for char in container:
        print(char)

    print("Recorrido reverso:")
    for char in container.reverse_iterator():
        print(char)

