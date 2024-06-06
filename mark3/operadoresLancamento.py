from pyautogui import *
import pyperclip
import pyscreeze
import time
import utils


def escreverValorUnit(valor_unit_convertido, passos=6):
    press(["right"]*passos)
    valor_unit_convertido = utils.formatador(valor_unit_convertido, casas_decimais="{:.6f}")
    time.sleep(0.2)
    write(valor_unit_convertido)
    time.sleep(0.2)
    press(["right"]*3)
 
 
def verificarValorDoItem(lista, indiceX):
    razoes = []
    time.sleep(0.7)
    cancelar_lancamento = False
    press(["right"]*4)
    time.sleep(0.7)
    hotkey("ctrl", "c")
    time.sleep(0.7)
    valor_do_item_no_siga = pyperclip.paste()
    valor_do_item_no_siga = utils.formatador4(valor_do_item_no_siga)
    valor_do_item_na_NF = lista[indiceX][0]
    valor_do_item_na_NF = utils.formatador3(valor_do_item_na_NF)
    if valor_do_item_no_siga != valor_do_item_na_NF:
        write(lista[indiceX][0])
        time.sleep(0.8)
        encontrar = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\valitenErrado.png')
        if type(encontrar) == pyscreeze.Box:
            press("enter")
            press("esc")
            press(["left"]*5)
            time.sleep(0.2)
            hotkey("ctrl", "c", interval=0.5)
            quantidade_siga = pyperclip.paste()
            quantidade_siga = utils.formatador3(quantidade_siga)
            quantidade_NF = lista[indiceX][1]
            quantidade_NF = utils.formatador3(quantidade_NF)
            valor_unit_NF = lista[indiceX][2]
            valor_unit_NF = utils.formatador3(valor_unit_NF)
            if quantidade_siga == quantidade_NF:
                escreverValorUnit(valor_unit_NF, passos=1)
            else:
                press(["left"]*5)
                time.sleep(0.2)
                hotkey("ctrl", "c", interval=0.5)
                desc_prod = pyperclip.paste()
                desc_prod = desc_prod.lower()
                if "abracadeira" in desc_prod:
                    quantidade_convertida = quantidade_NF * 100
                    if quantidade_convertida == quantidade_siga:
                        valor_unit_convertido = valor_unit_NF / 100
                        escreverValorUnit(valor_unit_convertido)
                    else:
                        quantidade_total = utils.contarItemFracionado(quantidade_siga, valor_unit_convertido, quantidade_convertida)
                        if sum(quantidade_total) != quantidade_convertida:
                            cancelar_lancamento = True
                            utils.cancelarLancamento()
                            utils.mudarSelecao()
                        else:
                            for qtd in quantidade_total:
                                razao = qtd / quantidade_convertida
                                razoes.append(razao)
                            press(["right"]*3)
                elif "gas" in desc_prod or "pedrisco" in desc_prod or "cabo" in desc_prod:
                    valor_unit_convertido = valor_do_item_na_NF / quantidade_siga
                    escreverValorUnit(valor_unit_convertido)
                else:
                    quantidade_total = utils.contarItemFracionado(quantidade_siga, valor_unit_NF, quantidade_NF)
                    if sum(quantidade_total) != quantidade_NF:
                        cancelar_lancamento = True
                        utils.cancelarLancamento()
                        utils.mudarSelecao()
                    else:
                        for qtd in quantidade_total:
                            razao = qtd / quantidade_NF
                            razoes.append(razao)
                        press(["right"]*3)
        else:
            press("left")
    return cancelar_lancamento, razoes


def copiarNatureza():
    press("right", interval=0.7)
    hotkey("ctrl", "c")
    time.sleep(0.7)
    natureza = pyperclip.paste()
    if natureza == "2020081":
        natureza = "2050006"
        press("enter")
        write(natureza)
    elif natureza in ["2020082", "2020083"]:
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
    desc_no_item = utils.formatador2(desc_no_item)
    write(desc_no_item, interval=0.02)
    time.sleep(0.5)


def inserirFrete(frete_no_item):
    press(["right"]*105)
    time.sleep(0.6)
    press("enter")
    frete_no_item = utils.formatador2(frete_no_item)
    write(frete_no_item, interval=0.05)
    time.sleep(0.6)


def inserirSeguro(seg_no_item):
    time.sleep(0.3)
    press("enter")
    seg_no_item = utils.formatador2(seg_no_item)
    write(seg_no_item, interval=0.05)
    time.sleep(0.6)


def inserirDespesa(desp_no_item):
    time.sleep(0.3)
    press("enter")
    desp_no_item = utils.formatador2(desp_no_item)
    write(desp_no_item, interval=0.05)
    time.sleep(0.6)
    press(["left"]*112)


def inserirICMS(icms_no_item, bc_icms, aliq_icms):
    press(["right"]*7)
    time.sleep(0.5)
    press("enter")
    bc_icms = utils.formatador2(bc_icms)
    write(bc_icms)
    press(["right"]*8)
    time.sleep(0.5)
    press("enter")
    write(aliq_icms)
    time.sleep(0.5)
    press(["left"]*9)
    time.sleep(0.5)
    press("enter")
    icms_no_item = utils.formatador2(icms_no_item)
    write(icms_no_item)


def inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST, passosST=9):
    press(["right"]*passosST)
    time.sleep(0.4)
    press("enter")
    base_icms_ST = utils.formatador2(base_icms_ST)
    write(base_icms_ST)
    time.sleep(0.4)
    press("enter")
    write(aliq_icms_ST)
    time.sleep(0.4)
    press("enter")
    icmsST_no_item = utils.formatador2(icmsST_no_item)
    write(icmsST_no_item)
    press(["left"]*12)    
    

def inserirIPI(ipi_no_item, base_ipi, aliq_ipi, passosIPI=12):
    press(["right"]*passosIPI)
    time.sleep(0.5)
    press("enter")
    base_ipi = utils.formatador2(base_ipi)
    write(base_ipi)
    press(["right"]*5)
    time.sleep(0.5)
    press("enter")
    write(aliq_ipi)
    press(["left"]*6)
    time.sleep(0.5)
    press("enter")
    ipi_no_item = utils.formatador2(ipi_no_item)
    write(ipi_no_item)
    press(["left"]*14)
