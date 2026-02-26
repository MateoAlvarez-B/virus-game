import random
from cartas import Carta

class Mazo:
    def __init__(self):
        self.cartas = []
        self.descartes = []
        self._crear_mazo()
        self.barajar()

    def _crear_mazo(self):
        # Aquí luego añadiremos todas las cartas reales del juego
        pass

    def barajar(self):
        random.shuffle(self.cartas)

    def robar(self):
        if not self.cartas:
            self.cartas = self.descartes
            self.descartes = []
            self.barajar()
        return self.cartas.pop()

    def descartar(self, carta):
        self.descartes.append(carta)
