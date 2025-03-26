def collatz_iterations(n):
    """Calcula la cantidad de iteraciones hasta que la secuencia converge a 1."""
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def generate_collatz_data(limit=10000):
    """Genera los datos de iteraciones para cada número inicial."""
    return [(n, collatz_iterations(n)) for n in range(1, limit + 1)]

def plot_ascii_chart(data, width=50):
    """Genera una representación en ASCII del gráfico de Collatz."""
    max_iterations = max(count for _, count in data)
    scale = max(1, max_iterations // width)  # Ajustar escala para el ancho
    
    print("\nGráfico ASCII de la Conjetura de Collatz")
    print("Eje X: Número de Iteraciones | Eje Y: Número Inicial (n)\n")

    for n, iterations in data:
        scaled_iterations = iterations // scale  # Reducimos ancho según la escala
        bar = "*" * scaled_iterations
        print(f"{str(n).rjust(5)} | {bar}")

if __name__ == "__main__":
    collatz_data = generate_collatz_data(100)
    plot_ascii_chart(collatz_data)

