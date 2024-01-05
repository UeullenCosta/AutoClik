from Calculos import Calculos
from filtro_de_planilha import Filtro_de_planilha
from Movimentacao import Movimentacao
from planilha import Planilha
import pandas as pd
import numpy as np
import pyautogui as pgui
planilha = Planilha()
calculo = Calculos()
movimento = Movimentacao()
filtro = Filtro_de_planilha()

#INICIANDO CLASSE CHAO
class Chao:
    def ch_laterais(self):
        COMP = pgui.prompt(text='Digite o comprimento do az ou box', title='MARQUINHOS')
        LARGURA = pgui.prompt(text='Digite o largura do az ou box', title='MARQUINHOS')
        ped = pgui.prompt(text='Digite a altura da ref do az ou box', title='MARQUINHOS')
        COMP = float(COMP)
        LARGURA = float(LARGURA)
        ped = float(ped)
        planilha.set_pe(ped)
        planilha.set_comprimento(COMP)
        planilha.set_largura(LARGURA)
        # iniciando
        movimento.iniciacao()
        cont = True
        while (cont):
            planilha.set_contador()
            df = pd.read_excel("pontos.xls")
            tbRef = df["Unnamed: 0"].replace(np.nan, "0")
            tbDist = df["Unnamed: 1"].replace(np.nan, 0)
            tbAngl = df["Unnamed: 2"].replace(np.nan, 0)
            # iniciando contagem
            c = planilha.get_contador()
            calculo.set_radiandos(tbAngl[c])
            calculo.set_distancia(tbDist[c])
            calculo.set_altura(tbDist[c])

            nome = tbRef[c]
            nome = str(nome).upper()

            if (nome == "FIM"):
                cont = False

            if (nome == "DIST FD"):
                # calculo
                distancia = calculo.get_distancia()
                # planilha
                planilha.set_distancia(distancia)

            if (nome == "DIST FT"):
                # calculo
                distancia = calculo.get_distancia()
                # planilha
                comp = planilha.get_comprimento()
                distancia = comp - distancia
                planilha.set_distancia(distancia)

            if (nome == "DIST LD"):
                distancia = calculo.get_distancia()
                planilha.set_distref(distancia)

            if (nome == "DIST LE"):
                # calculo
                distancia = calculo.get_distancia()
                # planilha
                larg = planilha.get_largura()
                distancia = larg - distancia
                planilha.set_distref(distancia)

            if (nome == "CH LD"):
                filtro.set_referenciaPonto("P LD")
                n = planilha.get_distref()
                pt = calculo.get_distancia()

                if (pt > n):
                    pt = 0.05
                    distfd = planilha.get_distancia()
                    refalt = calculo.get_altura()
                    refalt = refalt * -1
                    planilha.set_altura(refalt)
                    altp = calculo.get_altura()
                    altp = altp * -1
                    movimento.lanca_ponto(distfd, refalt, pt, altp)
                else:
                    pt = n - pt
                    distfd = planilha.get_distancia()
                    refalt = calculo.get_altura()
                    refalt = refalt * -1
                    planilha.set_altura(refalt)
                    altp = calculo.get_altura()
                    altp = altp * -1
                    movimento.lanca_ponto(distfd, refalt, pt, altp)
            if (nome == "CH FD"):
                filtro.set_referenciaPonto("P FD")

            if (nome == "CH LE"):
                filtro.set_referenciaPonto("P LE")
                # CALCULO
                refalt = calculo.get_altura()
                pt = calculo.get_distancia()
                # planilha
                refalt = refalt * -1
                planilha.set_altura(refalt)
                distfd = planilha.get_distancia()
                n = planilha.get_distref()
                pt = n + pt
                movimento.lanca_ponto(distfd, refalt, pt, refalt)

            if (nome == "CH FT"):
                filtro.set_referenciaPonto("P FT")

            if (nome == "AT LD"):
                filtro.set_referenciaPonto("P LD")
                n = planilha.get_distref()
                pt = calculo.get_distancia()

                if (pt > n):
                    pt = 0.05
                    distfd = planilha.get_distancia()
                    refalt = planilha.get_altura()
                    altp = calculo.get_altura()
                    altp = altp * -1
                    movimento.lanca_ponto(distfd, refalt, pt, altp)
                else:
                    pt = n - pt
                    distfd = planilha.get_distancia()
                    refalt = planilha.get_altura()

                    altp = calculo.get_altura()
                    altp = altp * -1
                    movimento.lanca_ponto(distfd, refalt, pt, altp)

            n1 = filtro.get_referenciaPonto()
            if (nome == "0" and n1 == "P LE"):
                # planillha
                distfd = planilha.get_distancia()
                refalt = planilha.get_altura()
                n = planilha.get_distref()
                # calculo
                pt = calculo.get_distancia()
                pt = pt + n
                altp = calculo.get_altura()
                altp = altp * -1
                # movimento
                movimento.lanca_ponto(distfd, refalt, pt, altp)

            n1 = filtro.get_referenciaPonto()
            if (nome == "0" and n1 == "P LD"):
                n = planilha.get_distref()
                pt = calculo.get_distancia()

                if (pt > n):
                    pt = 0.05
                    distfd = planilha.get_distancia()
                    refalt = planilha.get_altura()

                    altp = calculo.get_altura()
                    altp = altp * -1
                    movimento.lanca_ponto(distfd, refalt, pt, altp)
                else:
                    pt = n - pt
                    distfd = planilha.get_distancia()
                    refalt = planilha.get_altura()

                    altp = calculo.get_altura()
                    altp = altp * -1
                    movimento.lanca_ponto(distfd, refalt, pt, altp)


            if (nome == "AT LE"):
                filtro.set_referenciaPonto("P LE")
                # planilha
                distfd = planilha.get_distancia()
                refalt = planilha.get_altura()
                n = planilha.get_distref()
                # calculo
                pt = calculo.get_distancia()
                pt = pt + n
                altp = calculo.get_altura()
                altp = altp * -1
                # movimento
                movimento.lanca_ponto(distfd, refalt, pt, altp)
                # filtro

            else:
                pass
    def ch_fretes(self):
        COMP = pgui.prompt(text='Digite o comprimento do az ou box', title='MARQUINHOS')
        LARGURA = pgui.prompt(text='Digite o largura do az ou box', title='MARQUINHOS')
        ped = pgui.prompt(text='Digite a altura da ref do az ou box', title='MARQUINHOS')
        COMP = float(COMP)
        LARGURA = float(LARGURA)
        ped = float(ped)
        planilha.set_pe(ped)
        planilha.set_comprimento(COMP)
        planilha.set_largura(LARGURA)
        # iniciando
        movimento.iniciacao()
        cont = True
        while (cont):
            planilha.set_contador()
            df = pd.read_excel("pontos.xls")
            tbRef = df["Unnamed: 0"].replace(np.nan, "0")
            tbDist = df["Unnamed: 1"].replace(np.nan, 0)
            tbAngl = df["Unnamed: 2"].replace(np.nan, 0)
            # iniciando contagem
            c = planilha.get_contador()
            calculo.set_radiandos(tbAngl[c])
            calculo.set_distancia(tbDist[c])
            calculo.set_altura(tbDist[c])

            nome = tbRef[c]
            nome = str(nome).upper()

            if (nome == "FIM"):
                cont = False

            if (nome == "DIST FD"):
                # calculo
                distancia = calculo.get_distancia()
                # planilha
                planilha.set_distref(distancia)

            if (nome == "DIST FT"):
                # calculo
                distancia = calculo.get_distancia()
                # planilha
                comp = planilha.get_comprimento()
                distancia = comp - distancia
                planilha.set_distref(distancia)

            if (nome == "DIST LD"):
                distancia = calculo.get_distancia()
                planilha.set_distancia(distancia)

            if (nome == "DIST LE"):
                # calculo
                distancia = calculo.get_distancia()
                # planilha
                larg = planilha.get_largura()
                distancia = larg - distancia
                planilha.set_distancia(distancia)

            if (nome == "CH FD"):
                filtro.set_referenciaPonto("P FD")
                n = planilha.get_distref()
                pt = calculo.get_distancia()

                if (pt > n):
                    pt = 0.05
                    distfd = planilha.get_distancia()
                    refalt = calculo.get_altura()
                    refalt = refalt * -1
                    planilha.set_altura(refalt)
                    altp = calculo.get_altura()
                    altp = altp * -1
                    movimento.lanca_ponto(distfd, refalt, pt, altp)
                else:
                    pt = n - pt
                    distfd = planilha.get_distancia()
                    refalt = calculo.get_altura()
                    refalt = refalt * -1
                    planilha.set_altura(refalt)
                    altp = calculo.get_altura()
                    altp = altp * -1
                    movimento.lanca_ponto(distfd, refalt, pt, altp)

            if (nome == "CH LD"):
                filtro.set_referenciaPonto("P LD")

            if (nome == "CH FT"):
                filtro.set_referenciaPonto("P FT")
                # CALCULO
                refalt = calculo.get_altura()
                pt = calculo.get_distancia()
                # planilha
                refalt = refalt * -1
                planilha.set_altura(refalt)
                distfd = planilha.get_distancia()
                n = planilha.get_distref()
                pt = n + pt
                movimento.lanca_ponto(distfd, refalt, pt, refalt)

            if (nome == "CH LE"):
                filtro.set_referenciaPonto("P LE")

            if (nome == "AT FT"):
                filtro.set_referenciaPonto("P FT")
                # planilha
                distfd = planilha.get_distancia()
                refalt = planilha.get_altura()
                n = planilha.get_distref()
                # calculo
                pt = calculo.get_distancia()
                pt = pt + n
                altp = calculo.get_altura()
                altp = altp * -1
                # movimento
                movimento.lanca_ponto(distfd, refalt, pt, altp)
                # filtro


            n1 = filtro.get_referenciaPonto()
            if (nome == "0" and n1 == "P FT"):
                # planillha
                distfd = planilha.get_distancia()
                refalt = planilha.get_altura()
                n = planilha.get_distref()
                # calculo
                pt = calculo.get_distancia()
                pt = pt + n
                altp = calculo.get_altura()
                altp = altp * -1
                # movimento
                movimento.lanca_ponto(distfd, refalt, pt, altp)

            if (nome == "AT FD"):
                filtro.set_referenciaPonto("P FD")

                n = planilha.get_distref()
                pt = calculo.get_distancia()

                if (pt > n):
                    pt = 0.05
                    distfd = planilha.get_distancia()
                    refalt = planilha.get_altura()

                    altp = calculo.get_altura()
                    altp = altp * -1
                    movimento.lanca_ponto(distfd, refalt, pt, altp)
                else:
                    pt = n - pt
                    distfd = planilha.get_distancia()
                    refalt = planilha.get_altura()

                    altp = calculo.get_altura()
                    altp = altp * -1
                    movimento.lanca_ponto(distfd, refalt, pt, altp)

            n1 = filtro.get_referenciaPonto()
            if (nome == "0" and n1 == "P FD"):
                n = planilha.get_distref()
                pt = calculo.get_distancia()

                if (pt > n):
                    pt = 0.05
                    distfd = planilha.get_distancia()
                    refalt = planilha.get_altura()

                    altp = calculo.get_altura()
                    altp = altp * -1
                    movimento.lanca_ponto(distfd, refalt, pt, altp)
                else:
                    pt = n - pt
                    distfd = planilha.get_distancia()
                    refalt = planilha.get_altura()

                    altp = calculo.get_altura()
                    altp = altp * -1
                    movimento.lanca_ponto(distfd, refalt, pt, altp)


            else:
                pass
