import math
class Calculos:
    '''Classe de calculo dos valores que serão importados da planinha,
    esta planinha será importada por outra classe que por sua vez vai fazer a chamada dos metodos '''
    def __init__(self):
         self.radiandos = 0.0
         self.altura = 0.0
         self.distancia = 0.0
          ##Calculo dos Radiandos para obtenção de distancia e altura

    def get_radiandos(self):
        return self.radiandos
     

    def set_radiandos(self, altura1):
        angulo = math.radians(altura1)
        self.radiandos = angulo
        ##Calculo de distancia  cos


    def get_distancia(self):
        return self.distancia


    def set_distancia(self, dist):
        dist = math.cos(self.radiandos) * dist
        self.distancia =dist
        ## Calculo de Altuara com seno 

    def get_altura(self):
        return self.altura
    

    def set_altura(self, alt):
        radi = self.radiandos
        alt = math.sin(radi) * alt
        self.altura = alt


