class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        self.cuerpo = {}

    def robar(self, mazo):
        carta = mazo.robar()
        self.mano.append(carta)

    def jugar_carta(self, carta):
        self.mano.remove(carta)
