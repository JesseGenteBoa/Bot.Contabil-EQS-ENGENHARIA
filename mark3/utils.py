from pyautogui import locateOnScreen, locateCenterOnScreen, hotkey, press, write
from pydirectinput import click as mouseClique, moveTo
import pyscreeze
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
            x, y = locateCenterOnScreen(imagem, grayscale=True, confidence=0.92)
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
    variavel = variavel.replace(".", ",")
    return variavel

def formatador2(variavel):
    variavel = float(variavel)
    variavel = "{:.2f}".format(variavel)
    return variavel

def formatador3(variavel):
    variavel = variavel.replace(",", ".")
    variavel = float(variavel)
    return variavel

def formatador4(variavel):
    variavel = variavel.replace(".", "")
    variavel = formatador3(variavel)
    return variavel

def descerECopiar():
    press("down", interval=0.1)
    hotkey("ctrl", "c", interval=0.1)

def clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsiga.png'):
    x, y = encontrarImagemLocalizada(imagem)
    mouseClique(x, y)

def voltarEDescer(passos=1):
    hotkey(["shift", "tab"]*passos, interval=0.15)
    press("down")

def reiniciarPortal():
    clicarMicrosiga()
    voltarEDescer(passos=3)

def insistirNoClique(imagem, cliques=2):
    while True:
        try:
            clicarMicrosiga()
            time.sleep(1.5)
            try:
                mouseClique(250, 150)
                elemento = encontrarImagemLocalizada(imagem)
                a, b = elemento
                time.sleep(0.5)
                mouseClique(a,b, clicks=cliques, interval=0.1)
                time.sleep(0.5)
                break
            except:
                time.sleep(0.3)
        except:
            moveTo(100, 150)
            time.sleep(0.3)


def clicarDadosDaNota():
    imagem = r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\DadosDaNota.png'
    encontrar = encontrarImagemLocalizada(imagem)
    if type(encontrar) != tuple:            
        insistirNoClique(imagem)
        time.sleep(0.5)
    else:
        x, y = encontrar
        mouseClique(x,y, clicks=2)
    try:
        aparece_enter = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\NCMsegue.png')
        if type(aparece_enter) == pyscreeze.Box:
            time.sleep(0.5)
            press("enter")
    finally:
        write("408")     


def cancelarLancamento():
    cancelar_lancamento_click = encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\CancelarLancamento.png')
    x, y = cancelar_lancamento_click
    time.sleep(0.5)
    mouseClique(x,y, clicks=3, interval=0.1)
    while True:
        cancelar_lancamento_click = encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\salvarLancamento.png')
        if type(cancelar_lancamento_click) == tuple:
            mouseClique(x,y, clicks=2, interval=0.1)
        else:
            break
    aguarde = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
    while type(aguarde) == pyscreeze.Box:
        aguarde = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
        time.sleep(1)


def mudarSelecao():
    mudar_a_selecao = encontrarImagemLocalizada(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\mudarASelecao.png')
    x, y = mudar_a_selecao
    mouseClique(x,y, clicks=4, interval=0.4)
    time.sleep(1)
