from pyautogui import *
import pydirectinput
import time

def encontrarImagem(imagem):
    cont = 0
    while True:
        try:
            encontrou = locateOnScreen(imagem, grayscale=True, confidence = 0.8)
            return encontrou
        except:
            time.sleep(1)
            cont += 1
            if cont == 3:
                break
            print("Imagem não encontrada")
            pass

def encontrarImagemLocalizada(imagem):
    cont = 0
    while True:
        try:
            x, y = locateCenterOnScreen(imagem, grayscale=True, confidence=0.89)
            return (x, y)
        except:
            time.sleep(1)
            cont += 1
            if cont == 3:
                break
            print("Imagem não encontrada")
            pass

def formatador(variavel, casas_decimais="{:.2f}"):
    variavel = float(variavel)
    variavel = casas_decimais.format(variavel)
    variavel = str(variavel)
    variavel = variavel.replace(".", ",")
    return variavel

def formatador2(variavel):
    variavel = float(variavel)
    variavel = "{:.2f}".format(variavel)
    variavel = str(variavel)
    return variavel

def formatador3(variavel):
    variavel = variavel.replace(",", ".")
    variavel = float(variavel)
    return variavel

def formatador4(variavel):
    valor_parcela = valor_parcela.replace(".", "")
    formatador3(variavel)
    return variavel

def descerECopiar():
    press("down", interval=0.1)
    hotkey("ctrl", "c", interval=0.1)

def clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsiga.png'):
    x, y = encontrarImagemLocalizada(imagem)
    pydirectinput.click(x, y)

def voltarEDescer(passos=1):
    hotkey(["shift", "tab"]*passos, interval=0.15)
    press("down")

def reiniciarPortal():
    clicarMicrosiga()
    voltarEDescer(passos=3)