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

class Terca:

    def Tercas(self):

        COMP = pgui.prompt(text='Digite o comprimento entre terças', title='MARQUINHOS')
        LARGURA = pgui.prompt(text='Digite o largura do az ou box', title='MARQUINHOS')
        PE = pgui.prompt(text='Digite a altura do pé direito', title='MARQUINHOS')
        COMP = float(COMP)
        LARGURA = float(LARGURA)
        PE = float(PE)
        planilha.set_pe(PE)
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

            if (nome == "T"):
                # calculo
                distancia = calculo.get_distancia()
                terca = planilha.get_comprimento()
                # planilha
                distancia = distancia * terca
                planilha.set_distancia(distancia)

            if (nome == "DIST T"):
                # calculo
                distancia = planilha.get_distancia()
                distancia = distancia + calculo.get_distancia()
                # planilha
                planilha.set_distancia(distancia)

            if(nome == "DIAG LE/FD" or nome == "DIAG LE/FT"):
                filtro.set_referenciaPonto("P FD")

            if (nome == "DIAG LD/FD" or nome == "DIAG LD/FT"):
                filtro.set_referenciaPonto("P FD")

            if (nome == "DIAG FT/LD" or nome == "DIAG FT/LE"):
                filtro.set_referenciaPonto("P FD")

            if (nome == "DIAG FD/LD" or nome == "DIAG FD/LE"):
                filtro.set_referenciaPonto("P FD")

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
                filtro.set_referenciaPonto("P LD")
                # planilha
                n = planilha.get_distref()
                # calculo
                pt = calculo.get_distancia()
                if(pt > n):
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
                n = planilha.get_distref()
                # calculo
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
                # planilha
                n = planilha.get_distref()
                # calculo
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

