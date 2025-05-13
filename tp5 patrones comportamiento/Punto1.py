class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, number):
        if self.next_handler:
            return self.next_handler.handle(number)
        else:
            return f"{number} no consumido."


class PrimeHandler(Handler):
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            return f"{number} consumido por PrimeHandler."
        else:
            return super().handle(number)


class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            return f"{number} consumido por EvenHandler."
        else:
            return super().handle(number)


# Cadena de responsabilidad
handler_chain = PrimeHandler(EvenHandler())

# 1 al 100
for i in range(1, 101):
    print(handler_chain.handle(i))

