import pyautogui
import pyperclip
import pyscreeze
import time
import utils


def verificarValorDoItem(lista, indiceX):
        cancelar_lancamento = False
        pyautogui.press(["right"]*4)
        time.sleep(0.7)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.7)
        valor_do_item_no_siga = pyperclip.paste()
        valor_do_item_no_siga = valor_do_item_no_siga.replace(".", "")
        valor_do_item_no_siga = valor_do_item_no_siga.replace(",", ".")
        valor_do_item_na_NF = lista[indiceX][0]
        if valor_do_item_no_siga != valor_do_item_na_NF:
            pyautogui.write(lista[indiceX][0])
            time.sleep(0.3)
            encontrar = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\valitenErrado.png')
            if type(encontrar) == pyscreeze.Box:
                pyautogui.press("enter")
                pyautogui.press("esc")
                pyautogui.press(["left"]*5)
                time.sleep(0.2)
                pyautogui.hotkey("ctrl", "c", interval=0.5)
                quantidade_siga = pyperclip.paste()
                if quantidade_siga == lista[indiceX][1]:
                    pyautogui.press("right")
                    time.sleep(0.2)
                    pyautogui.write(lista[indiceX][2])
                    time.sleep(0.2)
                    pyautogui.press(["right"]*3)
                else:
                    cancelar_lancamento = True
                    clicar2 = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\CancelarLancamento.png')
                    time.sleep(0.5)
                    pyautogui.click(clicar2, clicks=3, interval=0.1)
                    aguarde = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
                    while type(aguarde) == pyscreeze.Box:
                        aguarde = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
                        time.sleep(1)
                    utils.voltarEDescer()
                    time.sleep(0.3)
                    time.sleep(0.3)
                    utils.clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsigaSelecionado.png')
            else:
                pyautogui.press("left")
        return cancelar_lancamento


def copiarNatureza():
    pyautogui.press("right", interval=0.7)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.7)
    natureza = pyperclip.paste()
    if natureza == "2020081":
        natureza = "2050006"
        pyautogui.press("enter")
        pyautogui.write(natureza)
    elif natureza in ["2020082", " 2020083"]:
        natureza = "2050008"
        pyautogui.press("enter")
        pyautogui.write(natureza)
        pyautogui.press("enter")
        pyautogui.press("left")
    
    return natureza


def selecionarCaso(natureza):
    codigo = {
    "2020067": 0, "2020085": 0, "2020047": 0, "2020049": 0, "2020055": 0,
    "2020045": 0, "2020006": 0, "2020041": 0, "2020048": 0, "2020042": 0,
    "2020046": 0, "2020030": 0, "2020031": 0, "2020074": 0, "2020019": 0,
    "2020040": 0, "2020056": 0, "2020075": 0, "2010016": 0,
    "2010005": 1, "2020027": 1, "2020036": 1,
    "2050003": 2, "2050004": 2, "2050005": 2, "2050006": 2,
    "2050007": 2, "2050008": 2, "2050009": 2,
    "2050001": 3,
    "2040005": 4,
    "2020029": 5, "2020053": 5,
    "2020018": 6, "2040001": 6, "2040003": 6
}
    return codigo.get(natureza, 7)


def definirTES(codigo, ctrl_imposto):
    pyautogui.press(["left"]*10)
    global tes
    if codigo == 0:
        if ctrl_imposto != 0:
            tes = "421"
        else:
            tes = "420"
    elif codigo == 1:
        if ctrl_imposto == 0:
            tes = "402"
        elif ctrl_imposto in [6,1,2]:
            tes = "405"
        elif ctrl_imposto == 7:
            tes = "407"
        else:
            tes = "403"
    elif codigo == 2:
        if ctrl_imposto not in [7, 5, 4, 3]:
            tes = "408"
        else:
            tes = "411"
    elif codigo == 3:
        tes = "423"
    elif codigo == 4:
        if ctrl_imposto not in [7, 5, 4, 3]:
            tes = "102"
        else:
            tes = "432"
    elif codigo == 5:
        pyautogui.hotkey("ctrl", "c", interval=0.5)
        tes_padrao = pyperclip.paste()
        if tes_padrao == "406":
            tes = "406"
        else:
            if ctrl_imposto == 0:
                tes = "402"
            elif ctrl_imposto == 7:
                tes = "407"
            elif ctrl_imposto in [6,1,2]:
                tes = "405"
            else:
                tes = "403"
    elif codigo == 6:
        pyautogui.hotkey("ctrl", "c", interval=0.5)
        tes_padrao = pyperclip.paste()
        if tes_padrao == "406":
            tes = "406"
        else:
            pyautogui.press(["left"]*2)
            time.sleep(0.7)
            pyautogui.hotkey("ctrl", "c", interval=0.5)
            item_especifico = pyperclip.paste()
            pyautogui.press(["right"]*2)
            if item_especifico in ["1303100449", "1303100601", "1303100602", "1303100603", "1312000122", "1312000124", "1312000125", "1312000126", "1312000144", "1308002", "1312024", "1303100550", "1303100600", "1303101290", "1303101291", "1303103835", "1303103836", "1303103837", "1312000141"]:
                if ctrl_imposto != 0:
                    tes = "421"
                else:
                    tes = "420"
            else:
                if ctrl_imposto == 0:
                    tes = "402"
                elif ctrl_imposto in [6,1,2]:
                    tes = "405"
                elif ctrl_imposto == 7:
                    tes = "407"
                else:
                    tes = "403"
    elif codigo == 7:
        cancelar_lancamento = True
        clicar2 = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\CancelarLancamento.png')
        time.sleep(0.3)
        pyautogui.click(clicar2)
        aguarde = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
        while type(aguarde) == pyscreeze.Box:
            aguarde = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
            time.sleep(1)
        utils.voltarEDescer()
        time.sleep(0.3)
        time.sleep(0.3)
        utils.clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsigaSelecionado.png')
        tes = cancelar_lancamento

    return tes
    

def zerarImposto(passos_ida=7, passos_volta=8):
    pyautogui.press(["right"]*passos_ida)
    pyautogui.press("enter")
    pyautogui.press("backspace")
    pyautogui.press("enter")
    pyautogui.press(["left"]*passos_volta)


def escreverTES(tes):
    pyautogui.press("enter", interval=0.3)
    pyautogui.write(tes)
    pyautogui.press(["right"]*4)


def inserirDesconto(desc_no_item):
    pyautogui.press(["right"]*3)
    time.sleep(0.4)
    pyautogui.press("enter")
    pyautogui.write(desc_no_item)
    pyautogui.press(["left"]*4)


def inserirICMS(icms_no_item, bc_icms, aliq_icms):
    pyautogui.press(["right"]*7)
    time.sleep(0.4)
    pyautogui.press("enter")
    pyautogui.write(bc_icms)
    pyautogui.press(["right"]*8)
    time.sleep(0.4)
    pyautogui.press("enter")
    pyautogui.write(aliq_icms)
    time.sleep(0.4)
    pyautogui.press(["left"]*9)
    time.sleep(0.4)
    pyautogui.press("enter")
    pyautogui.write(icms_no_item)


def inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST, passosST=9):
    pyautogui.press(["right"]*passosST)
    time.sleep(0.4)
    pyautogui.press("enter")
    pyautogui.write(base_icms_ST)
    time.sleep(0.4)
    pyautogui.press("enter")
    pyautogui.write(aliq_icms_ST)
    time.sleep(0.4)
    pyautogui.press("enter")
    pyautogui.write(icmsST_no_item)

    
def inserirIPI(ipi_no_item, base_ipi, aliq_ipi, passosIPI=12):
    pyautogui.press(["right"]*passosIPI)
    time.sleep(0.4)
    pyautogui.press("enter")
    pyautogui.write(base_ipi)
    pyautogui.press(["right"]*5)
    time.sleep(0.4)
    pyautogui.press("enter")
    pyautogui.write(aliq_ipi)
    pyautogui.press(["left"]*6)
    time.sleep(0.4)
    pyautogui.press("enter")
    pyautogui.write(ipi_no_item)
    pyautogui.press(["left"]*14)