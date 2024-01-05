from planilha import Planilha
import pyautogui as pgui
from lancaBox import LancaBox
from chao import Chao
from terca import Terca
import datetime
chao = Chao()
lancaBox = LancaBox()
planilha = Planilha()
terca = Terca()
txt = True
data = datetime.date(2024, 11, 30)
data = data.month
dataAtual = datetime.datetime.now().month

if (data >= dataAtual):
    txt = True
else:
    print("OLA O SEU LANÇADOR ESTÁ DESATUALIZADO SOLICITE A ATUALIZAÇÃO PARA O COLABORADOR UEULLEN")

if(txt == True):
    while(txt != "NONE"):
        print(
            "SEJA BEM VINDO ...\n LANÇADOR DE PONTOS CRIADO POR UEULLEN JUNIOR PEREIRA DA COSTA, \n INSPETOR DO SMA DA SGS")

        txt = pgui.prompt(text='Digite uma opção \n 1: P LD/LE \n 2: P FD/FT \n 3: CH LD/LE \n 4: CH FD/FT \n 5 TERÇAS',
                          title='MARQUINHOS')
        txt = str(txt).upper()
        if(txt == "1"):
            lancaBox.pontoLateral()

        if(txt == "2"):
            lancaBox.pontoFrente()

        if(txt == "3"):
            chao.ch_laterais()

        if(txt == "4"):
            chao.ch_fretes()

        if(txt == "5"):
            terca.Tercas()

    print(txt)