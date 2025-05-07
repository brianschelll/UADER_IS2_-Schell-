import os

class Ping:
    """
    Clase que realiza pings a direcciones IP.
    - execute: solo permite IPs que empiezan con '192.'
    - executefree: permite cualquier dirección
    """
    def execute(self, ip: str):
        if ip.startswith("192."):
            print(f"[Ping] Ejecutando ping controlado a {ip}")
            self._do_ping(ip)
        else:
            print(f"[Ping] Dirección IP no permitida: {ip}")

    def executefree(self, ip: str):
        print(f"[Ping] Ejecutando ping libre a {ip}")
        self._do_ping(ip)

    def _do_ping(self, ip: str):
        # Realiza 10 intentos de ping
        for i in range(10):
            print(f"Intento {i + 1}:")
            if os.name == 'nt':
                os.system(f"ping -n 1 {ip}")  
            else:
                os.system(f"ping -c 1 {ip}")  

class PingProxy:
    """
    Proxy que decide cómo ejecutar el ping:
    - Si IP es '192.168.0.254', redirige a ping libre a www.google.com
    - En cualquier otro caso, reenvía a Ping.execute()
    """
    def __init__(self):
        self._ping = Ping()

    def execute(self, ip: str):
        if ip == "192.168.0.254":
            print("[PingProxy] Dirección especial detectada. Redirigiendo ping libre a www.google.com")
            self._ping.executefree("www.google.com")
        else:
            print(f"[PingProxy] Reenviando ejecución a Ping con IP: {ip}")
            self._ping.execute(ip)

# ------------------ Pruebas ------------------

if __name__ == "__main__":
    proxy = PingProxy()

    # Caso especial
    proxy.execute("192.168.0.254")

    # Caso permitido por control
    proxy.execute("192.168.1.1")

    # Caso bloqueado por control
    proxy.execute("10.0.0.1")
