from pyautogui import *
from pydirectinput import click as mouseClique
import pyperclip
import pyscreeze
import time
import utils


def verificarValorDoItem(lista, indiceX):
        time.sleep(0.7)
        cancelar_lancamento = False
        press(["right"]*4)
        time.sleep(0.7)
        hotkey("ctrl", "c")
        time.sleep(0.7)
        valor_do_item_no_siga = pyperclip.paste()
        valor_do_item_no_siga = valor_do_item_no_siga.replace(".", "")
        valor_do_item_na_NF = lista[indiceX][0]
        if valor_do_item_no_siga != valor_do_item_na_NF:
            write(lista[indiceX][0])
            time.sleep(0.5)
            encontrar = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\valitenErrado.png')
            if type(encontrar) == pyscreeze.Box:
                press("enter")
                press("esc")
                press(["left"]*5)
                time.sleep(0.2)
                hotkey("ctrl", "c", interval=0.5)
                quantidade_siga = pyperclip.paste()
                if quantidade_siga == lista[indiceX][1]:
                    press("right")
                    time.sleep(0.2)
                    write(lista[indiceX][2])
                    time.sleep(0.2)
                    press(["right"]*3)
                else:
                    cancelar_lancamento = True
                    utils.cancelarLancamento()
                    mudar_a_selecao = utils.encontrarImagemLocalizada(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\mudarASelecao.png')
                    x, y = mudar_a_selecao
                    mouseClique(x,y, clicks=4, interval=0.4)
                    time.sleep(1)
            else:
                press("left")
        return cancelar_lancamento


def copiarNatureza():
    press("right", interval=0.7)
    hotkey("ctrl", "c")
    time.sleep(0.7)
    natureza = pyperclip.paste()
    if natureza == "2020081":
        natureza = "2050006"
        press("enter")
        write(natureza)
    elif natureza in ["2020082", " 2020083"]:
        natureza = "2050008"
        press("enter")
        write(natureza)
        press("enter")
        press("left")
    
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
    press(["left"]*10)
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
        hotkey("ctrl", "c", interval=0.5)
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
        hotkey("ctrl", "c", interval=0.5)
        tes_padrao = pyperclip.paste()
        if tes_padrao == "406":
            tes = "406"
        else:
            press(["left"]*2)
            time.sleep(0.7)
            hotkey("ctrl", "c", interval=0.5)
            item_especifico = pyperclip.paste()
            press(["right"]*2)
            if item_especifico in ["999949011000", "1303102887", "1302578", "1303100449", "1303100601", "1303100602", "1303100603", "1312000122", "1312000124", "1312000125", "1312000126", "1312000144", "1308002", "1312024", "1303100550", "1303100600", "1303101290", "1303101291", "1303103835", "1303103836", "1303103837", "1312000141"]:
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
        utils.cancelarLancamento()
        utils.voltarEDescer()
        time.sleep(0.3)
        tes = cancelar_lancamento

    return tes
    

def zerarImposto(passos_ida=7, passos_volta=8):
    press(["right"]*passos_ida)
    press("enter")
    press("backspace")
    press("enter")
    press(["left"]*passos_volta)


def escreverTES(tes):
    press("enter", interval=0.3)
    write(tes)
    press(["right"]*4)


def inserirDesconto(desc_no_item):
    press(["right"]*3)
    time.sleep(0.5)
    press("enter")
    write(desc_no_item, interval=0.02)
    time.sleep(0.5)


def inserirFrete(frete_no_item):
    press(["right"]*105)
    time.sleep(0.6)
    press("enter")
    write(frete_no_item, interval=0.05)
    time.sleep(0.6)


def inserirSeguro(seg_no_item):
    time.sleep(0.3)
    press("enter")
    write(seg_no_item, interval=0.05)
    time.sleep(0.6)


def inserirDespesa(desp_no_item):
    time.sleep(0.3)
    press("enter")
    write(desp_no_item, interval=0.05)
    time.sleep(0.6)
    press(["left"]*112)


def inserirICMS(icms_no_item, bc_icms, aliq_icms):
    press(["right"]*7)
    time.sleep(0.5)
    press("enter")
    write(bc_icms)
    press(["right"]*8)
    time.sleep(0.5)
    press("enter")
    write(aliq_icms)
    time.sleep(0.5)
    press(["left"]*9)
    time.sleep(0.5)
    press("enter")
    write(icms_no_item)


def inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST, passosST=9):
    press(["right"]*passosST)
    time.sleep(0.4)
    press("enter")
    write(base_icms_ST)
    time.sleep(0.4)
    press("enter")
    write(aliq_icms_ST)
    time.sleep(0.4)
    press("enter")
    write(icmsST_no_item)
    press(["left"]*12)    
    

def inserirIPI(ipi_no_item, base_ipi, aliq_ipi, passosIPI=12):
    press(["right"]*passosIPI)
    time.sleep(0.5)
    press("enter")
    write(base_ipi)
    press(["right"]*5)
    time.sleep(0.5)
    press("enter")
    write(aliq_ipi)
    press(["left"]*6)
    time.sleep(0.5)
    press("enter")
    write(ipi_no_item)
    press(["left"]*14)