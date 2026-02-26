from mazo import Mazo
from jugador import Jugador
from ia import IA

class MotorJuego:
    def __init__(self):
        self.mazo = Mazo()
        self.jugador = Jugador("Jugador")
        self.ia = IA("IA")

    def iniciar(self):
        print("=== Bienvenido a Virus! ===")
        # Aquí luego implementaremos el flujo del juego
        pass
