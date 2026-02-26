class Cuerpo:
    def __init__(self):
        self.organos = {
            "corazon": None,
            "cerebro": None,
            "estomago": None,
            "hueso": None
        }

    def estado(self, organo):
        return self.organos[organo]
