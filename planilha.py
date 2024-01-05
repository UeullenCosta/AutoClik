class Planilha:
    def __init__(self):
        self.distancia = 0.0
        self.altura = 0.0
        self.ponto = 0.0
        self.at = 0.0
        self.distref = 0.0
        self.contador = 0
        self.comprimento = 0.0
        self.largura = 0.0
        self.pe = 0.0

    def get_distancia(self):
        return self.distancia

    def get_altura(self):
        return self.altura

    def get_distref(self):
        return self.distref

    def get_contador(self):
        return self.contador

    def get_ponto(self):
        return self.ponto

    def get_at(self):
        return self.at

    def get_comprimento(self):
        return self.comprimento

    def get_largura(self):
        return self.largura

    def get_pe(self):
        return self.pe

    def set_comprimento(self, comp):
        self.comprimento = comp

    def set_largura(self, larg):
        self.largura = larg

    def set_pe(self, pe):
        self.pe = pe

    def set_ponto(self, dist):
        self.ponto = dist

    def set_at(self, at):
        self.at = at

    def set_distancia(self, dist):
        self.distancia = dist

    def set_altura(self, alt):
        self.altura = alt

    def set_distref(self, distref):
        self.distref = distref

    def set_contador(self):
        self.contador += 1