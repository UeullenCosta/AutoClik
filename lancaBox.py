from Calculos import Calculos
from filtro_de_planilha import Filtro_de_planilha
import pyautogui as pgui
from Movimentacao import Movimentacao
from planilha import Planilha
import pandas as pd
import numpy as np
import openpyxl

planilha = Planilha()
calculo = Calculos()
movimento = Movimentacao()
filtro = Filtro_de_planilha()
class LancaBox:

    def pontoLateral(self):

        COMP = pgui.prompt(text='Digite o comprimento do az ou box', title='MARQUINHOS')
        LARGURA = pgui.prompt(text='Digite o largura do az ou box', title='MARQUINHOS')
        ped = pgui.prompt(text='Digite a altura da ref do az ou box', title='MARQUINHOS')
        COMP = float(COMP)
        LARGURA = float(LARGURA)
        ped = float(ped)
        planilha.set_pe(ped)
        planilha.set_comprimento(COMP)
        planilha.set_largura(LARGURA)
        #iniciando
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

            if (nome == "REF FD"):
                # calculo
                altura = calculo.get_altura()
                distancia = calculo.get_distancia()
                # planilha
                planilha.set_distancia(distancia)
                pe = planilha.get_pe()
                altura = pe - altura
                planilha.set_altura(altura)

            if (nome == "REF FT"):
                # calculo
                altura = calculo.get_altura()
                distancia = calculo.get_distancia()
                # planilha
                comp = planilha.get_comprimento()
                planilha.set_distancia(distancia - comp)
                pe = planilha.get_pe()
                altura = pe - altura
                planilha.set_altura(altura)

            if (nome == "REF LD"):
                # calculo
                altura = calculo.get_altura()
                distancia = calculo.get_distancia()
                # planilha
                pe = planilha.get_pe()
                planilha.set_distref(distancia)
                altura = pe - altura
                planilha.set_altura(altura)

            if (nome == "REF LE"):
                # calculo
                altura = calculo.get_altura()
                Distancia = calculo.get_distancia()
                # planilha
                larg = planilha.get_largura()
                planilha.set_distref(larg - Distancia)
                pe = planilha.get_pe()
                altura = pe - altura
                planilha.set_altura(altura)

            if (nome == "P LD"):
                # planilha
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

            if (nome == "P FD"):
                filtro.set_referenciaPonto("P FD")

            if (nome == "P LE"):
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
            if (nome == "P FT"):
                filtro.set_referenciaPonto("P FT")
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
                # planilha
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

    def pontoFrente(self):
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

            if (nome == "REF FD"):
                # calculo
                altura = calculo.get_altura()
                distancia = calculo.get_distancia()
                # planilha
                planilha.set_distref(distancia)
                pe = planilha.get_pe()
                planilha.set_altura(pe + (altura * -1))

            if (nome == "REF FT"):
                # calculo
                altura = calculo.get_altura()
                distancia = calculo.get_distancia()
                # planilha
                comp = planilha.get_comprimento()
                planilha.set_distref(comp - distancia)
                pe = planilha.get_pe()
                planilha.set_altura(pe + (altura * -1))

            if (nome == "REF LD"):
                # calculo
                altura = calculo.get_altura()
                distancia = calculo.get_distancia()
                # planilha
                pe = planilha.get_pe()
                planilha.set_distancia(distancia)
                planilha.set_altura(pe + (altura * -1))

            if (nome == "REF LE"):
                # calculo
                Altura = calculo.get_altura()
                Distancia = calculo.get_distancia()
                # planilha
                larg = planilha.get_largura()
                planilha.set_distancia(larg - Distancia)
                pe = planilha.get_pe()
                planilha.set_altura(pe + (Altura * -1))

            if (nome == "P FD"):
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

            if (nome == "P LD"):
                filtro.set_referenciaPonto("P LD")

            if (nome == "P FT"):
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
            if (nome == "P LE"):
                filtro.set_referenciaPonto("P LE")

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

            if (nome == "AT FD"):
                filtro.set_referenciaPonto("P FD")
                # planilha
                distfd = planilha.get_distancia()
                refalt = planilha.get_altura()
                n = planilha.get_distref()
                # calculo
                pt = calculo.get_distancia()
                pt = n - pt
                altp = calculo.get_altura()
                altp = altp * -1
                movimento.lanca_ponto(distfd, refalt, pt, altp)

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

            else:
                pass