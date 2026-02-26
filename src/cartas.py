class Carta:
    def __init__(self, tipo, subtipo=None):
        self.tipo = tipo          # "organo", "virus", "medicina", "especial"
        self.subtipo = subtipo    # corazón, cerebro, trasplante, etc.

    def __repr__(self):
        return f"{self.tipo}:{self.subtipo}"
