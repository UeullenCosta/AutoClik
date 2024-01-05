import pyautogui as pgui
import time
class Movimentacao:
    def iniciacao(self,):
        pgui.PAUSE = 0.1

        pgui.moveTo(x=766, y=753, duration= 0.2)
        pgui.click(x=766, y=753)
        pgui.click(x=766, y=753)
        pgui.press('up')
        pgui.moveTo(x=766, y=450, duration=0.2)
        pgui.click(x=766, y=450)
        pgui.write("4")
        pgui.press('Enter')
        pgui.press('right')

        pgui.moveTo(x=469, y=447, duration=0.2)
        pgui.click(x=469, y=447)
        pgui.write("4")
        pgui.press('Enter')
        pgui.press('up')

        pgui.moveTo(x=766, y=753, duration=0.2)
        pgui.click(x=766, y=753)
        pgui.write("4")
        pgui.press('Enter')
        pgui.moveTo(x=766, y=653, duration=0.2)
        pgui.moveTo(x=766, y=753, duration=0.2)
        time.sleep(0.2)
        pgui.write("4")
        pgui.press('Enter')
        pgui.click(x=766, y=753)
        pgui.click(x=766, y=753)
        pgui.press('Esc')
        pgui.press('Esc')

    def lanca_ponto(self, dist, ref, pt, alt):
        #puchando ponto
        pgui.PAUSE = 0.1
    #iniciando
        pgui.moveTo(x=766, y=753, duration= 0.2)
        pgui.click(x=766, y=753)
        pgui.press('left')
    #distancia do fundo
        pgui.moveTo(x=1068, y=670, duration=0.2)
        pgui.click(x=1068, y=670)
        dist = format(dist, '.2f').replace(".",",")
        pgui.write(dist)
        pgui.press('Enter')
        pgui.press('up')
    #subindo referencia
        pgui.moveTo(x=766, y=450, duration=0.2)
        pgui.click(x=766, y=450)
        ref = format(ref, '.2f').replace(".",",")
        ref
        pgui.write(ref)
        pgui.press('Enter')
        pgui.press('right')
    #lancando ponto
        pgui.moveTo(x=469, y=447, duration=0.2)
        pgui.click(x=469, y=447)
        pt = format(pt, '.2f').replace(".",",")
        pgui.write(pt)
        pgui.press('Enter')
        pgui.press('up')
    #Altura do ponto
        pgui.moveTo(x=766, y=753, duration=0.2)
        alt = format(alt, '.2f').replace(".",",")
        pgui.write(alt)
        pgui.press('Enter')
        time.sleep(0.1)
        pgui.press('esc')
        time.sleep(0.1)
        pgui.press('esc')

    def lanca_pp(self, dist, ref, pp):

        # puchando ponto
        pgui.PAUSE = 0.1
        # iniciando
        pgui.moveTo(x=766, y=753, duration=0.2)
        pgui.click(x=766, y=753)
        pgui.press('left')
        # distancia do fundo
        pgui.moveTo(x=1068, y=670, duration=0.2)
        pgui.click(x=1068, y=670)
        pgui.write(dist)
        pgui.press('Enter')
        pgui.press('up')
        # subindo referencia
        pgui.moveTo(x=766, y=450, duration=0.2)
        pgui.click(x=766, y=450)
        pgui.write(ref)
        pgui.press('Enter')
        pgui.press('up')
        # lancando ponto
        pgui.moveTo(x=766, y=753, duration=0.2)
        pgui.click(x=766, y=753)
        pgui.write(pp)
        pgui.press('Enter')
        time.sleep(0.1)
        pgui.press('esc')
        time.sleep(0.1)
        pgui.press('esc')
