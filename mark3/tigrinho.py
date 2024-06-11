from pyautogui import hotkey, press, write
from pydirectinput import click as mouseClique, moveTo
import pyperclip        
import time
import xmltodict   
import pyscreeze
import utils
import extratorXML
import tratamentoItem
import operadoresLancamento
from selenium import webdriver                         
from selenium.webdriver.common.by import By

processos_ja_vistos = []
contador = 0
cnpj_dict = {'80464753000197': '02', '80464753000430': '04', '80464753000510': '05', '80464753000782': '07', '80464753000863': '08', '80464753000944': '09', '80464753001088': '10', '80464753001169': '11', '80464753001240': '12', '80464753001320': '13', '80464753001401': '14', '80464753001592': '15', '80464753001673': '16', '80464753001916': '19', '80464753002050': '20', '80464753002130': '21', '80464753002211': '22', '80464753002564': '25', '80464753002645': '26', '80464753002807': '28', '80464753002998': '29', '80464753003021': '30', '80464753003102': '31', '80464753003293': '32', '80464753003374': '33', '80464753003617': '34', '80464753003536': '35', '80464753003455': '36', '80464753003706': '37', '80464753003960': '39', '80464753004001': '40', '80464753004184': '41', '80464753004265': '42', '80464753004346': '43', '80464753004699': '46', '80464753004770': '47', '80464753004850': '48', '80464753004931': '49', '80464753005075': '50', '80464753005156': '51', '80464753005407': '54', '80464753005580': '55', '80464753005660': '56', '80464753005741': '57', '80464753005822': '58', '80464753005903': '59', '80464753006047': '60'}
FAILSAFE = True


def robozinho():
    ver_documento = r'C:\Users\Usuario\Desktop\mark4\Imagens\verDocumentos.png'
    utils.insistirNoClique(ver_documento, cliques=1)
    time.sleep(0.4)
    insistir_no_clique = utils.encontrarImagem(ver_documento)
    if type(insistir_no_clique) == pyscreeze.Box:
        while True:
            utils.insistirNoClique(ver_documento, cliques=1)
            insistir_no_clique = utils.encontrarImagem(ver_documento)
            if type(insistir_no_clique) != pyscreeze.Box:
                break
    hotkey("alt", "d", interval=0.1)
    time.sleep(0.5)
    hotkey("ctrl", "c")
    time.sleep(0.5)
    link = pyperclip.paste()
    options = webdriver.ChromeOptions()
    options.add_argument(r'user-data-dir=C:\Users\Usuario\AppData\Local\Google\Chrome\User Data\Profile Selenium')
    driver = webdriver.Chrome(options=options)
    time.sleep(0.5)
    driver.get(link)
    time.sleep(2)
    tempo_max = 0

    while True:
        try:
            elemento1 = driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/app-processo-pagamento-nota-manutencao/po-page-default/po-page/div/po-page-content/div/div[2]/po-tabs/div[1]/div/po-tab-button[2]/div/span')
            time.sleep(0.3)
            elemento1.click()
            
            if elemento1 != '':
                try:
                    elemento2 = driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/app-processo-pagamento-nota-manutencao/po-page-default/po-page/div/po-page-content/div/div[1]/div[1]/po-widget/div/po-container/div/div/po-info[5]/div/div[2]/span')
                    chave_de_acesso = elemento2.text
                    try:
                        verificador = processos_ja_vistos.index(chave_de_acesso)
                        time.sleep(0.3)
                        hotkey("alt", "tab", interval=0.1)
                        hotkey("ctrl", "w")
                        time.sleep(0.2)
                        utils.reiniciarPortal()
                        time.sleep(0.2)
                        driver.quit()
                        time.sleep(0.2)
                        return robozinho() 

                    except:
                        processos_ja_vistos.append(chave_de_acesso)
                        
                    elemento3 = driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/app-processo-pagamento-nota-manutencao/po-page-default/po-page/div/po-page-content/div/div[2]/po-tabs/div[2]/po-tab[2]/div[1]/po-select/po-field-container/div/div[2]/select')
                    valor = elemento3.get_attribute("value")

                    if valor == 'B':
                        try:
                            elemento4 = driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/app-processo-pagamento-nota-manutencao/po-page-default/po-page/div/po-page-content/div/div[2]/po-tabs/div[2]/po-tab[2]/div[2]/po-table/po-container/div/div/div/div/div/table/tbody/tr/td[4]/div/span/div[3]/po-input/po-field-container/div/div[2]/input')
                            boleto = elemento4.get_attribute("value")
                            if len(boleto) == 0:
                                time.sleep(0.2)
                                utils.reiniciarPortal()
                                time.sleep(0.2)
                                driver.quit()
                                time.sleep(0.2)
                                return robozinho()
                            else:
                                driver.quit() 
                                break

                        except Exception as e:
                            tempo_max += 1 
                            pass  

                    else:
                        driver.quit() 
                        break                                           

                except Exception as e:
                    tempo_max += 1 
                    pass  

        except Exception as e:
            tempo_max += 1 
            pass
        
        if tempo_max == 15:
            press("enter")
        if tempo_max == 40:
            time.sleep(0.3)
            hotkey("alt", "tab", interval=0.1)
            hotkey("ctrl", "w")
            time.sleep(0.2)
            utils.reiniciarPortal()
            time.sleep(0.2)
            driver.quit()
            time.sleep(0.2)
            return robozinho()  
   
    time.sleep(0.2)
    hotkey("ctrl", "w")
    time.sleep(0.3)


    caminho = "C:\\Users\\Usuario\\Desktop\\mark4\\xmlFiscalio\\" + chave_de_acesso + ".xml"

    while True:
        try:
            with open(caminho) as fd:
                doc = xmltodict.parse(fd.read())
                break
        except UnicodeDecodeError:
            with open(caminho, encoding='utf-8') as fd:
                doc = xmltodict.parse(fd.read())
                break
        except FileNotFoundError:
            while True:
                exportarXML = r'C:\Users\Usuario\Desktop\mark4\Imagens\exportarXML.png'
                encontrar = utils.encontrarImagemLocalizada
                if type(encontrar) != tuple:  
                    utils.insistirNoClique(exportarXML)
                    time.sleep(2)
                    caixa_de_texto = utils.encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\clicarServidor.png')
                    if type(caixa_de_texto) == tuple:
                        break
                else:
                    x, y = encontrar
                    mouseClique(x,y, clicks=2)
                    break
            time.sleep(2)
            x, y = caixa_de_texto
            mouseClique(x,y, clicks=3, interval=0.07)
            pyperclip.copy("C:\\Users\\Usuario\\Desktop\\mark4\\xmlFiscalio\\")
            hotkey("ctrl", "v")
            time.sleep(1)
            press(["tab"]*6, interval=0.5)
            press("enter")
            time.sleep(0.8)
            caixa_de_texto = utils.encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\clicarServidor.png')
            if type(caixa_de_texto) == tuple:
                botao_salvar = utils.encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\botaoSalvar1.png')
                x, y = botao_salvar
                mouseClique(x,y, clicks=2)
            cont=0
            while True:
                aparece_enter = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\XMLEnter.png')
                if type(aparece_enter) == pyscreeze.Box:
                    press("enter")
                    time.sleep(0.8)
                aparece_enter2 = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\XMLEnter2.png')
                if type(aparece_enter2) == pyscreeze.Box:
                    break
            while type(aparece_enter2) == pyscreeze.Box:
                press("enter")
                time.sleep(0.5)
                aparece_enter2 = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\XMLEnter2.png')
            caminho = "C:\\Users\\Usuario\\Desktop\\mark4\\xmlFiscalio\\" + chave_de_acesso + ".xml"
            auxiliar = False
        except:
            auxiliar = True
        if auxiliar == True:
            hotkey(["tab"]*3, interval=0.1)
            press("down")
            time.sleep(0.5)
            utils.clicarMicrosiga()
            return robozinho()
        
        
    processador = extratorXML.ProcessadorXML(doc, cnpj_dict)
    valor_total_da_nf, filial_xml = processador.processarTotaisNotaFiscal()

    const_item = 0
    while True:
        try:
            coletor_xml = doc["nfeProc"]["NFe"]["infNFe"]["det"]["prod"]
            impostos_xml = doc["nfeProc"]["NFe"]["infNFe"]["det"]["imposto"]
            valores_do_item = processador.coletarDadosXML(coletor_xml, impostos_xml)
            break
        except TypeError:
            try:
                coletor_xml = doc["nfeProc"]["NFe"]["infNFe"]["det"][const_item]["prod"]
                impostos_xml = doc["nfeProc"]["NFe"]["infNFe"]["det"][const_item]["imposto"]
                valores_do_item = processador.coletarDadosXML(coletor_xml, impostos_xml)
                const_item += 1
            except IndexError:
                break

    itens, indices_e_impostos = processador.trabalharDadosXML(valores_do_item)

    utils.clicarDadosDaNota()
    time.sleep(1)
    while True:
        press("tab")
        time.sleep(0.7)
        hotkey("ctrl", "c")
        filial_pedido = pyperclip.paste()
        if filial_pedido == filial_xml:
            press("tab", interval=0.5)
            press("enter")
            time.sleep(1)
            clicar_confirmar = utils.encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\clicarConfirmar.png')
            if type(clicar_confirmar) == tuple:
                x, y = clicar_confirmar
                mouseClique(x,y, clicks=2, interval=0.07)
            break
        else:
            try:
                clicar_cancelar = utils.encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\CancelarFilial.png')
                x, y = clicar_cancelar
                mouseClique(x,y, clicks=2, interval=0.07)
                utils.cancelar1()
                return robozinho()
            except TypeError:
                utils.clicarDadosDaNota()

    try:
        time.sleep(0.5)
        aparece_enter = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\AtencaoEstoque.png')
        if type(aparece_enter) == pyscreeze.Box:
            time.sleep(0.2)
            press("enter")
        aparece_enter2 = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\TES102.png')
        if type(aparece_enter2) == pyscreeze.Box:
            time.sleep(0.2)
            press("enter")
            time.sleep(0.2)
            press(["tab"]*2)
            time.sleep(0.2)
            write("102")
            time.sleep(0.2)
            press(["tab"]*2, interval=0.5)
            time.sleep(0.2)
            press("enter") 
    finally:
        pass

    cont = 0
    while True:
        time.sleep(1)
        tela_de_lancamento = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\AbriuOProcesso.png')
        cont +=1
        if type(tela_de_lancamento) == pyscreeze.Box:
            time.sleep(0.5)
            press(["tab"]*10)
            time.sleep(0.8)
            press(["right"]*8)
            break
        lancamento_retroativo = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\LancamentoRetroativo.png')
        nota_ja_lancada = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\ProcessoJaLancado.png')
        fornecedor_bloqueado = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\FornecedorBloqueado.png')
        if type(lancamento_retroativo) == pyscreeze.Box or type(nota_ja_lancada) == pyscreeze.Box or type(fornecedor_bloqueado) == pyscreeze.Box:
            time.sleep(1)
            press("enter")
            time.sleep(1)
            cont = 0
        erro_esquisito = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\erroEsquisito2.png')
        if type(erro_esquisito) == pyscreeze.Box:
            time.sleep(1)
            press("enter")
            utils.cancelar1()
            return robozinho()
        erro_generico = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\ErroGenerico.png')
        if type(erro_generico) == pyscreeze.Box:
            time.sleep(1)
            press("enter", interval=2) 
            press("esc", interval=2) 
            press("enter", interval=2)    
            utils.cancelar1()
            return robozinho()
        chave_nao_encontrada = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\chaveNaoEncontradaNoSefaz.png')
        if type(chave_nao_encontrada) == pyscreeze.Box:
            time.sleep(1)
            press("enter")
            utils.cancelar2()
            return robozinho()
        if cont == 20:
            press("enter")
            cont = 0
              

    for i, ctrl_imposto in enumerate(indices_e_impostos):

        verificador, item_fracionado = operadoresLancamento.verificarValorDoItem(itens, i)
        if verificador == True:
            return robozinho()
        tratamento_item = tratamentoItem.TratadorItem(item_fracionado, itens, i, ctrl_imposto)
        item = tratamento_item.tratarItem()
        cont = 0

        if ctrl_imposto == 0:
            for lista in item:
                desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, icmsST_no_item, ipi_no_item = lista
                natureza = operadoresLancamento.copiarNatureza()
                codigo = operadoresLancamento.selecionarCaso(natureza)
                tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
                if tes == True:
                    return robozinho()
                operadoresLancamento.escreverTES(tes)
                if tes in ["102", "405", "408"]:
                    operadoresLancamento.zerarImposto()
                elif tes in ["406", "421", "423"]:
                    operadoresLancamento.zerarImposto()
                    operadoresLancamento.zerarImposto(passos_ida=12, passos_volta=13)
                operadoresLancamento.inserirDesconto(desc_no_item)
                operadoresLancamento.inserirFrete(frete_no_item)
                operadoresLancamento.inserirSeguro(seg_no_item)
                operadoresLancamento.inserirDespesa(desp_no_item)
                press("down")
                cont+=1
                if len(item) > 1:
                    press(["right"]*4)
                    if cont == len(item):
                        press(["left"]*4)
            press("up")
                                      #SEQUENCIA LOGICA DE LANÇAMENTO SEM IMPOSTO
        elif ctrl_imposto == 1:
            for lista in item:
                desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, bc_icms, aliq_icms, icmsST_no_item, ipi_no_item = lista
                natureza = operadoresLancamento.copiarNatureza()
                codigo = operadoresLancamento.selecionarCaso(natureza)
                tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
                if tes == True:
                    return robozinho()
                operadoresLancamento.escreverTES(tes)
                if tes in ["406", "421", "423"]:
                    operadoresLancamento.zerarImposto(passos_ida=12, passos_volta=13)
                operadoresLancamento.inserirDesconto(desc_no_item)
                operadoresLancamento.inserirFrete(frete_no_item)
                operadoresLancamento.inserirSeguro(seg_no_item)
                operadoresLancamento.inserirDespesa(desp_no_item)
                operadoresLancamento.inserirICMS(icms_no_item, bc_icms, aliq_icms)
                press(["left"]*9)
                press("down")
                cont+=1
                if len(item) > 1:
                    press(["right"]*4)
                    if cont == len(item):
                        press(["left"]*4)
            press("up")
                                        #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMS
        elif ctrl_imposto == 2:
            for lista in item:
                desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, icmsST_no_item, base_icms_ST, aliq_icms_ST, ipi_no_item = lista
                natureza = operadoresLancamento.copiarNatureza()
                codigo = operadoresLancamento.selecionarCaso(natureza)
                tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
                if tes == True:
                    return robozinho()
                operadoresLancamento.escreverTES(tes)
                if tes in ["102", "405", "408"]:
                    operadoresLancamento.zerarImposto()
                elif tes in ["406", "421", "423"]:
                    operadoresLancamento.zerarImposto()
                    operadoresLancamento.zerarImposto(passos_ida=12, passos_volta=13)
                operadoresLancamento.inserirDesconto(desc_no_item)
                operadoresLancamento.inserirFrete(frete_no_item)
                operadoresLancamento.inserirSeguro(seg_no_item)
                operadoresLancamento.inserirDespesa(desp_no_item)
                operadoresLancamento.inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST)
                press("down")
                cont+=1
                if len(item) > 1:
                    press(["right"]*4)
                    if cont == len(item):
                        press(["left"]*4)
            press("up")
                                        #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMSST
        elif ctrl_imposto == 3:
            for lista in item:
                desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, icmsST_no_item, ipi_no_item, base_ipi, aliq_ipi = lista
                natureza = operadoresLancamento.copiarNatureza()
                codigo = operadoresLancamento.selecionarCaso(natureza)
                tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
                if tes == True:
                    return robozinho()
                operadoresLancamento.escreverTES(tes)
                if tes in ["406", "421", "423", "102", "403", "411"]:
                    operadoresLancamento.zerarImposto()
                operadoresLancamento.inserirDesconto(desc_no_item)
                operadoresLancamento.inserirFrete(frete_no_item)
                operadoresLancamento.inserirSeguro(seg_no_item)
                operadoresLancamento.inserirDespesa(desp_no_item)
                operadoresLancamento.inserirIPI(ipi_no_item, base_ipi, aliq_ipi)
                press("down")
                cont+=1
                if len(item) > 1:
                    press(["right"]*4)
                    if cont == len(item):
                        press(["left"]*4)
            press("up")
                                        #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA IPI
        elif ctrl_imposto == 4:
            for lista in item:
                desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, icmsST_no_item, base_icms_ST, aliq_icms_ST, ipi_no_item, base_ipi, aliq_ipi = lista
                natureza = operadoresLancamento.copiarNatureza()
                codigo = operadoresLancamento.selecionarCaso(natureza)
                tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
                if tes == True:
                    return robozinho()
                operadoresLancamento.escreverTES(tes)
                if tes in ["406", "421", "423", "102", "411"]:
                    operadoresLancamento.zerarImposto()
                operadoresLancamento.inserirDesconto(desc_no_item)
                operadoresLancamento.inserirFrete(frete_no_item)
                operadoresLancamento.inserirSeguro(seg_no_item)
                operadoresLancamento.inserirDespesa(desp_no_item)
                operadoresLancamento.inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST)
                operadoresLancamento.inserirIPI(ipi_no_item, base_ipi, aliq_ipi, passosIPI=0)
                press("down")
                cont+=1
                if len(item) > 1:
                    press(["right"]*4)
                    if cont == len(item):
                        press(["left"]*4)
            press("up")
                                         #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMSST E IPI
        elif ctrl_imposto == 5:
            for lista in item:
                desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, base_icms, aliq_icms, icmsST_no_item, ipi_no_item, base_ipi, aliq_ipi = lista
                natureza = operadoresLancamento.copiarNatureza()
                codigo = operadoresLancamento.selecionarCaso(natureza)
                tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
                if tes == True:
                    return robozinho()
                operadoresLancamento.escreverTES(tes)
                operadoresLancamento.inserirDesconto(desc_no_item)
                operadoresLancamento.inserirFrete(frete_no_item)
                operadoresLancamento.inserirSeguro(seg_no_item)
                operadoresLancamento.inserirDespesa(desp_no_item)
                operadoresLancamento.inserirICMS(icms_no_item, base_icms, aliq_icms)
                operadoresLancamento.inserirIPI(ipi_no_item, base_ipi, aliq_ipi, passosIPI=3)
                press("down")
                cont+=1
                if len(item) > 1:
                    press(["right"]*4)
                    if cont == len(item):
                        press(["left"]*4)
            press("up")
                                        #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMS E IPI
        elif ctrl_imposto == 6:
            for lista in item:
                desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, base_icms, aliq_icms, icmsST_no_item, base_icms_ST, aliq_icms_ST, ipi_no_item = lista
                natureza = operadoresLancamento.copiarNatureza()
                codigo = operadoresLancamento.selecionarCaso(natureza)
                tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
                if tes == True:
                    return robozinho()
                operadoresLancamento.escreverTES(tes)
                operadoresLancamento.inserirDesconto(desc_no_item)
                operadoresLancamento.inserirFrete(frete_no_item)
                operadoresLancamento.inserirSeguro(seg_no_item)
                operadoresLancamento.inserirDespesa(desp_no_item)
                operadoresLancamento.inserirICMS(icms_no_item, base_icms, aliq_icms)
                operadoresLancamento.inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST, passosST=0)
                press("down")
                cont+=1
                if len(item) > 1:
                    press(["right"]*4)
                    if cont == len(item):
                        press(["left"]*4)
            press("up")
                                            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMS E ICMSST
        elif ctrl_imposto == 7:
            for lista in item:
                desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, base_icms, aliq_icms, icmsST_no_item, base_icms_ST, aliq_icms_ST, ipi_no_item, base_ipi, aliq_ipi = lista
                natureza = operadoresLancamento.copiarNatureza()
                codigo = operadoresLancamento.selecionarCaso(natureza)
                tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
                if tes == True:
                    return robozinho()
                operadoresLancamento.escreverTES(tes)
                operadoresLancamento.inserirDesconto(desc_no_item)
                operadoresLancamento.inserirFrete(frete_no_item)
                operadoresLancamento.inserirSeguro(seg_no_item)
                operadoresLancamento.inserirDespesa(desp_no_item)
                operadoresLancamento.inserirICMS(icms_no_item, base_icms, aliq_icms)
                operadoresLancamento.inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST, passosST=0)
                operadoresLancamento.inserirIPI(ipi_no_item, base_ipi, aliq_ipi, passosIPI=12)
                press("down")
                cont+=1
                if len(item) > 1:
                    press(["right"]*4)
                    if cont == len(item):
                        press(["left"]*4)
            press("up")
                                        #SEQUENCIA LOGICA DE LANÇAMENTO PARA TODOS OS IMPOSTOS
 
        if len(indices_e_impostos) > 1:
            press("down")
        if i+1 == len(indices_e_impostos):
            press("up")
        time.sleep(1.5)


    aba_duplicatas = utils.encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\AbaDuplicatas.png')
    x, y =  aba_duplicatas
    mouseClique(x,y, clicks=4, interval=0.1)
    time.sleep(0.6)
    lista_parc = []
    utils.clicarValorParcela()
    time.sleep(0.5)
    hotkey("ctrl", "c", interval=0.2)
    valor_parcela = pyperclip.paste()
    valor_parcela = utils.formatador4(valor_parcela)
    if valor_parcela < valor_total_da_nf:
        lista_parc.append(valor_parcela)
        while round(sum(lista_parc),2) < valor_total_da_nf:
            utils.descerECopiar()
            valor_parcela = pyperclip.paste()
            valor_parcela = utils.formatador4(valor_parcela)
            lista_parc.append(valor_parcela)
        somatoria = utils.formatador2(sum(lista_parc))
        somatoria = float(somatoria)
        parcela_errada = lista_parc[-1]
        if somatoria != valor_total_da_nf:
            if lista_parc[-1] == lista_parc[-2]:
                parcela_errada = lista_parc.pop()
                somatoria = utils.formatador2(sum(lista_parc))
                somatoria = float(somatoria)
            diferenca_NF_siga = valor_total_da_nf - somatoria 
            ultima_parcela = parcela_errada + diferenca_NF_siga
            ultima_parcela = "{:.2f}".format(ultima_parcela)  
            mouseClique(x,y)
            descida = len(lista_parc) - 1
            press(["down"]*descida)
            time.sleep(0.4)
            write(ultima_parcela, interval=0.03)
        time.sleep(1)
    elif valor_parcela > valor_total_da_nf:
        valor_total_da_nf = utils.formatador2(valor_total_da_nf)
        write(valor_total_da_nf)
        time.sleep(1)
    utils.clicarNaturezaDuplicata()
    time.sleep(1)
    erro_parcela = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\ErroParcela.png')
    if type(erro_parcela) == pyscreeze.Box:
        press("enter")
        utils.clicarValorParcela()
        press(["left"]*2)
        time.sleep(0.3)
        hotkey("ctrl", "c", interval=0.1)
        primeira_parc = pyperclip.paste()
        ordem_parc = []
        ordem_parc.append(primeira_parc)
        if primeira_parc != '':
            utils.descerECopiar
            proxima_parcela = pyperclip.paste()
            ordem_parc.append(proxima_parcela)
            if ordem_parc[-2] != ordem_parc[-1]:
                while ordem_parc[-2] != ordem_parc[-1]:
                    utils.descerECopiar
                    proxima_parcela = pyperclip.paste()
                    ordem_parc.append(proxima_parcela)
                ordem_parc.pop()
                valor_parcela = valor_total_da_nf / len(ordem_parc)
                valor_parcela = "{:.2f}".format(valor_parcela)
                utils.clicarValorParcela()
                for vezes in range(len(ordem_parc)):
                    write(valor_parcela)
                    time.sleep(0.3)
                    press("down")
        utils.clicarNaturezaDuplicata()
        time.sleep(0.6)
        erro_parcela = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\ErroParcela.png')
        if type(erro_parcela) == pyscreeze.Box:
            press("enter")
            utils.cancelar2()
            return robozinho()
    hotkey("ctrl", "c", interval=0.2)
    natureza_perc = pyperclip.paste() 
    if natureza_perc != "0,00":
        lista_perc = []
        while round(sum(lista_perc),2) < 100.0:
            natureza_perc = utils.formatador3(natureza_perc)
            lista_perc.append(natureza_perc)
            utils.descerECopiar()
            natureza_perc = pyperclip.paste() 
        maior_perc = max(lista_perc)
        natureza_duplicata_clique = utils.encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\naturezaDuplicata.png')
        x, y = natureza_duplicata_clique
        mouseClique(x,y)
        press("up")
        time.sleep(0.2)
        hotkey("ctrl", "c", interval=0.1)
        perc_majoritario = pyperclip.paste()
        perc_majoritario = utils.formatador3(perc_majoritario)
        while perc_majoritario != maior_perc:
            utils.descerECopiar()
            perc_majoritario = pyperclip.paste()
            perc_majoritario = utils.formatador3(perc_majoritario)
        press("left")
        hotkey("ctrl", "c", interval=0.1)
        natureza_duplicata = pyperclip.paste()
        hotkey(["shift", "tab"]*5, interval=0.2)
        write(natureza_duplicata)
        press("tab")
        time.sleep(1)


    salvar = utils.encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\salvarLancamento.png')
    salvarx, salvary = salvar
    time.sleep(0.7)
    mouseClique(salvarx,salvary, clicks=2, interval=0.1)
    time.sleep(2)
    cont = 0
    while True:
        salvar = utils.encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\salvarLancamento.png')
        if type(salvar) == tuple:
            mouseClique(salvarx,salvary, clicks=2, interval=0.1)
            cont += 1
            time.sleep(1)
            if cont == 2:
                break
        else:
            break
    erro_de_serie = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\ErroDeSerie.png')
    if type(erro_de_serie) == pyscreeze.Box:
        press("enter", interval=0.2) 
        espec_doc = utils.encontrarImagemLocalizada(r'C:\Users\Usuario\Desktop\mark4\Imagens\CorrigirErroDeSerie.png')
        x, y = espec_doc
        time.sleep(0.5)
        mouseClique(x,y, clicks=2)
        write("NF", interval=0.1)
        press("enter")
        time.sleep(0.5)
        mouseClique(salvarx,salvary, clicks=2)
    erro_esquisito = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\erroEsquisito.png')
    if type(erro_esquisito) == pyscreeze.Box:
        press("esc")
        quit()
    erro_quantidade = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\erroDeQuantidade.png')
    if type(erro_quantidade) == pyscreeze.Box:
        press("enter")
        utils.cancelarLancamento()
        mudar_a_selecao = utils.encontrarImagemLocalizada(imagem=r'C:\Users\Usuario\Desktop\mark4\Imagens\mudarASelecao.png')
        x, y = mudar_a_selecao
        mouseClique(x,y, clicks=2)
        time.sleep(0.3)
        utils.clicarMicrosiga()
        return robozinho()

    cont = 0
    etapa_final = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\etapaFinal.png')
    while type(etapa_final) != pyscreeze.Box:
        time.sleep(0.2)
        etapa_final = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\etapaFinal.png')
    press(["tab"]*3, interval=0.9)
    press("enter")
    time.sleep(1.5)
    ultimo_enter = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\finalizarLancamento.png')
    if type(ultimo_enter) != pyscreeze.Box:
        while type(ultimo_enter) != pyscreeze.Box:
            time.sleep(0.2)
            ultimo_enter = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\finalizarLancamento.png')
            cont +=1
            if cont == 10:
                press("enter")
                cont = 0
    press("tab", interval=0.9)
    press("enter")
    aux = False
    cont2 = 0
    while True:
        ultima_tela = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\ultimaTela.png')
        if type(ultima_tela) == pyscreeze.Box:
            aux = True
            while type(ultima_tela) == pyscreeze.Box:
                ultima_tela = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\ultimaTela.png')
                time.sleep(0.2)
        if aux == True:
            break
        ultimo_enter = utils.encontrarImagem(r'C:\Users\Usuario\Desktop\mark4\Imagens\finalizarLancamento.png')
        if type(ultimo_enter) == pyscreeze.Box:
            cont +=1
            if cont == 5:
                aux = True
                press("enter")
        if cont2 == 3:
            break
        cont2 +=1
    

    hotkey("win", "d")
    time.sleep(0.2)
    
    return robozinho()


if __name__ == "__main__":
    robozinho()
