from pyautogui import locateOnScreen, locateCenterOnScreen, hotkey, press, position, write, FailSafeException
from pydirectinput import click as mouseClique, moveTo
from selenium import webdriver                         
from pyperclip import paste
from time import sleep
import pyscreeze



def checarFailsafe():
    z, f = position()
    if z == 0 and f == 0:
        raise FailSafeException
    

def encontrarImagem(imagem):
    cont = 0
    while True:
        try:
            encontrou = locateOnScreen(imagem, grayscale=True, confidence = 0.8)
            checarFailsafe()
            return encontrou
        except:
            sleep(0.8)
            cont += 1
            if cont == 3:
                break
            print("Imagem não encontrada")
            checarFailsafe()
            pass
            

def encontrarImagemLocalizada(imagem):
    cont = 0
    while True:
        try:
            x, y = locateCenterOnScreen(imagem, grayscale=True, confidence=0.92)
            checarFailsafe()      
            return (x, y)
        except:
            sleep(0.8)
            cont += 1
            if cont == 3:
                break
            print("Imagem não encontrada")
            checarFailsafe()
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
    checarFailsafe()

def clicarMicrosiga(imagem=r'C:\Users\Usuario\Desktop\mark4\Imagens\microsiga.png'):
    x, y = encontrarImagemLocalizada(imagem)
    mouseClique(x, y)
    checarFailsafe()

def mudarSelecao():
    mudar_a_selecao = encontrarImagemLocalizada(imagem=r'C:\Users\Usuario\Desktop\mark4\Imagens\mudarASelecao.png')
    x, y = mudar_a_selecao
    mouseClique(x,y, clicks=4, interval=0.4)
    sleep(1)
    checarFailsafe()

def voltarEDescer(passos=1):
    hotkey(["shift", "tab"]*passos, interval=0.15)
    press("down")
    checarFailsafe()

def reiniciarPortal():
    clicarMicrosiga()
    voltarEDescer(passos=3)
    checarFailsafe()

def cancelar1():
    sleep(0.8)
    voltarEDescer()
    sleep(0.5)
    clicarMicrosiga()
    checarFailsafe()

def cancelar2():
    sleep(0.5)
    cancelarLancamento()
    voltarEDescer()
    sleep(0.3)
    clicarMicrosiga()
    checarFailsafe()

def erroNoPortal():
    sleep(0.3)
    hotkey("alt", "tab", interval=0.1)
    hotkey("ctrl", "w")
    sleep(0.2)
    reiniciarPortal()
    sleep(0.2)
    checarFailsafe()

def cancelarEMudar():
    cancelarLancamento()
    mudarSelecao()
    checarFailsafe()

def escreverNatureza(natureza):
    press("enter")
    write(natureza)
    press("enter")
    press("left")
    checarFailsafe()


def insistirNoClique(imagem, cliques=2):
    while True:
        try:
            clicarMicrosiga()
            sleep(1.5)
            checarFailsafe()
            try:
                mouseClique(250, 150)
                checarFailsafe()
                elemento = encontrarImagemLocalizada(imagem)
                a, b = elemento
                sleep(0.5)
                mouseClique(a,b, clicks=cliques, interval=0.1)
                sleep(0.5)
                break
            except:
                sleep(0.3)
        except:
            moveTo(100, 150)
            sleep(0.3)
    checarFailsafe()


def clicarDadosDaNota(): 
    encontrar = encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\DadosDaNota.png')
    if type(encontrar) != tuple:            
        insistirNoClique(r'C:\Users\Usuario\Desktop\mark4\Imagens\DadosDaNota.png')
        sleep(0.5)
        checarFailsafe()
    else:
        x, y = encontrar
        mouseClique(x,y, clicks=2)
    try:
        aparece_enter = encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\NCMsegue.png')
        if type(aparece_enter) == pyscreeze.Box:
            sleep(0.5)
            press("enter")
            checarFailsafe()
    finally:
        write("408")
    checarFailsafe()


def cancelarLancamento():
    cancelar_lancamento_click = encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\CancelarLancamento.png')
    x, y = cancelar_lancamento_click
    sleep(0.5)
    mouseClique(x,y, clicks=3, interval=0.1)
    checarFailsafe()
    while True:
        cancelar_lancamento_click = encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\salvarLancamento.png')
        if type(cancelar_lancamento_click) == tuple:
            mouseClique(x,y, clicks=2, interval=0.1)
            checarFailsafe()
        else:
            break
    aguarde = encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\Aguarde.png') 
    while type(aguarde) == pyscreeze.Box:
        aguarde = encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\Aguarde.png') 
        sleep(1)
    checarFailsafe()

    

def contarItemFracionado(quantidade_siga, valor_unit, quantidade_real):
    valor_unit = formatador(valor_unit, casas_decimais="{:.6f}")
    cont = 0
    quantidade_total = []
    quantidade_total.append(quantidade_siga)
    press("left")
    sleep(0.2)
    hotkey("ctrl", "c", interval=0.5)
    cod_item = paste()
    checarFailsafe()
    try:
        while sum(quantidade_total) < quantidade_real:
            press("down")
            sleep(0.5)
            hotkey("ctrl", "c", interval=0.8)
            item_dividido = paste()
            cont+=1
            if item_dividido == cod_item:
                press(["right"]*6)
                hotkey("ctrl", "c", interval=0.8)
                qtd_dividida = paste()
                qtd_dividida = formatador4(qtd_dividida)
                quantidade_total.append(qtd_dividida)
                press("right")
                write(valor_unit, interval=0.05)
                press(["left"]*8)
                checarFailsafe()        
            else:
                break
    except TypeError:
        pass
    if len(quantidade_total) > 10:
        press(["up"]*cont, interval=20)
    else:
        press(["up"]*cont, interval=0.1)
    sleep(0.5)
    press(["right"]*7)
    sleep(0.5)
    write(valor_unit, interval=0.05)
    checarFailsafe()
    return quantidade_total


def clicarValorParcela():
    valor_parcela = encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\clicarParcela.png')
    while type(valor_parcela) != tuple:
        moveTo(180, 200)
        aba_duplicatas = encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\AbaDuplicatas.png')
        x, y =  aba_duplicatas
        checarFailsafe()
        mouseClique(x,y, clicks=4, interval=0.1)
        valor_parcela = encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\clicarParcela.png')
        sleep(0.4)
    x, y = valor_parcela
    mouseClique(x,y)
    checarFailsafe()


def clicarNaturezaDuplicata():
    while True:
        natureza_duplicata_clique = encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\naturezaDuplicata.png')
        checarFailsafe()
        if type(natureza_duplicata_clique) != tuple:
            moveTo(150, 250)
            mouseClique(x,y, clicks=4, interval=0.1)
            sleep(0.3)
        else:
            break
    x, y = natureza_duplicata_clique
    mouseClique(x,y)
    checarFailsafe()


def acrescerLista(lista, lista2, link):
    try:
        verificador = lista.index(link)
    except:
        lista.append(link)
    try:
        verificador = lista2.index(link)
    except:
        lista2.append(link)


def tratarLista(lista1, lista2):
    lista_unica = lista1 + lista2
    lista_unica = list(set(lista_unica))
    return lista_unica


def abrirLinkSelenium(lista):
    options = webdriver.ChromeOptions()
    options.add_argument(r'user-data-dir=C:\Users\Usuario\AppData\Local\Google\Chrome\User Data\Profile Selenium')
    driver = webdriver.Chrome(options=options)
    print(lista)
    if len(lista) > 1:
        try:
            driver.get(lista[0])
            for link in lista[1:]:
                sleep(0.2)
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[-1])
                sleep(0.5)
                driver.get(link)
            while True:
                sleep(1)
                if not driver.window_handles:
                    break
        except IndexError:
            pass
    else: 
        try:
            driver.get(lista[0])
            while True:
                sleep(1)
                if not driver.window_handles:
                    break
        except IndexError:
            driver.quit()
