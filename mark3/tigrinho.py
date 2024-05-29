from pyautogui import hotkey, press, write
from pydirectinput import click as mouseClique, moveTo
import pyperclip        
import time
import xmltodict   
import pyscreeze
import utils
import extratorXML
import operadoresLancamento
from selenium import webdriver                         
from selenium.webdriver.common.by import By

processos_ja_vistos = []
contador = 0
cnpj_dict = {'80464753000197': '02', '80464753000430': '04', '80464753000510': '05', '80464753000782': '07', '80464753000863': '08', '80464753000944': '09', '80464753001088': '10', '80464753001169': '11', '80464753001240': '12', '80464753001320': '13', '80464753001401': '14', '80464753001592': '15', '80464753001673': '16', '80464753001916': '19', '80464753002050': '20', '80464753002130': '21', '80464753002211': '22', '80464753002564': '25', '80464753002645': '26', '80464753002807': '28', '80464753002998': '29', '80464753003021': '30', '80464753003102': '31', '80464753003293': '32', '80464753003374': '33', '80464753003617': '34', '80464753003536': '35', '80464753003455': '36', '80464753003706': '37', '80464753003960': '39', '80464753004001': '40', '80464753004184': '41', '80464753004265': '42', '80464753004346': '43', '80464753004699': '46', '80464753004770': '47', '80464753004850': '48', '80464753004931': '49', '80464753005075': '50', '80464753005156': '51', '80464753005407': '54', '80464753005580': '55', '80464753005660': '56', '80464753005741': '57', '80464753005822': '58', '80464753005903': '59', '80464753006047': '60'}
FAILSAFE = True


def robozinho():
    ver_documento = r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\verDocumentos.png'
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
    options.add_argument(r'user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data\Perfil Selenium')
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
                            break

                        except Exception as e:
                            tempo_max += 1 
                            pass  

                    else:
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
        
    time.sleep(0.3)
    hotkey("alt", "tab")
    time.sleep(0.3)
    hotkey("ctrl", "w")
    time.sleep(0.3)


    caminho = "C:\\Users\\User\\OneDrive - EQS Engenharia Ltda\\Documentos\\GitHub\\GitHubDoJessezinho\\mark3\\xmlFiscalio\\" + chave_de_acesso + ".xml"

    try:
        with open(caminho) as fd:
            doc = xmltodict.parse(fd.read())
    except:
        driver.quit()
        while True:
            exportarXML = r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\exportarXML.png'
            encontrar = utils.encontrarImagemLocalizada
            if type(encontrar) != tuple:  
                utils.insistirNoClique(exportarXML)
                time.sleep(2)
                caixa_de_texto = utils.encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\clicarServidor.png')
                if type(caixa_de_texto) == tuple:
                    break
            else:
                x, y = encontrar
                mouseClique(x,y, clicks=2)
                break
        time.sleep(2)
        x, y = caixa_de_texto
        mouseClique(x,y, clicks=3, interval=0.07)
        pyperclip.copy("C:\\Users\\User\\OneDrive - EQS Engenharia Ltda\\Documentos\\GitHub\\GitHubDoJessezinho\\mark3\\xmlFiscalio\\")
        hotkey("ctrl", "v")
        time.sleep(1)
        press(["tab"]*6, interval=0.5)
        press("enter")
        time.sleep(1.5)
        press("enter")
        time.sleep(1.5)
        press("enter")
        time.sleep(3)
        caminho = "C:\\Users\\User\\OneDrive - EQS Engenharia Ltda\\Documentos\\GitHub\\GitHubDoJessezinho\\mark3\\xmlFiscalio\\" + chave_de_acesso + ".xml"
        auxiliar = False
        try:
            with open(caminho) as fd:
                doc = xmltodict.parse(fd.read())
        except:
            auxiliar = True
        if auxiliar == True:
            hotkey(["tab"]*3, interval=0.1)
            press("down")
            time.sleep(0.5)
            driver.quit()
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
            break
        else:
            try:
                clicar_cancelar = utils.encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\CancelarFilial.png')
                x, y = clicar_cancelar
                mouseClique(x,y, clicks=2, interval=0.07)
                utils.voltarEDescer()
                time.sleep(0.3)
                driver.quit()
                time.sleep(0.3)
                utils.clicarMicrosiga()
                return robozinho()
            except TypeError:
                utils.clicarDadosDaNota()

    try:
        time.sleep(0.5)
        aparece_enter = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\AtencaoEstoque.png')
        if type(aparece_enter) == pyscreeze.Box:
            time.sleep(0.2)
            press("enter")
        aparece_enter2 = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\TES102.png')
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
        tela_de_lancamento = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\AbriuOProcesso.png')
        cont +=1
        if type(tela_de_lancamento) == pyscreeze.Box:
            time.sleep(0.5)
            press(["tab"]*10)
            time.sleep(0.8)
            press(["right"]*8)
            break
        lancamento_retroativo = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\LancamentoRetroativo.png')
        nota_ja_lancada = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\ProcessoJaLancado.png')
        fornecedor_bloqueado = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\FornecedorBloqueado.png')
        if type(lancamento_retroativo) == pyscreeze.Box or type(nota_ja_lancada) == pyscreeze.Box or type(fornecedor_bloqueado) == pyscreeze.Box:
            time.sleep(1)
            press("enter")
            time.sleep(1)
            cont = 0
        erro_esquisito = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\erroEsquisito2.png')
        if type(erro_esquisito) == pyscreeze.Box:
            time.sleep(1)
            press("enter")
            time.sleep(1)
            utils.voltarEDescer()
            time.sleep(0.5)
            driver.quit()
            time.sleep(1)
            utils.clicarMicrosiga()
            return robozinho()
        erro_generico = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\ErroGenerico.png')
        if type(erro_generico) == pyscreeze.Box:
            time.sleep(1)
            press("enter", interval=2) 
            press("esc", interval=2) 
            press("enter", interval=2)    
            utils.voltarEDescer()
            time.sleep(0.5)
            driver.quit()
            time.sleep(1)
            utils.clicarMicrosiga()
            return robozinho()
        chave_nao_encontrada = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\chaveNaoEncontradaNoSefaz.png')
        if type(chave_nao_encontrada) == pyscreeze.Box:
            time.sleep(1)
            press("enter")
            time.sleep(1)
            utils.cancelarLancamento()
            utils.voltarEDescer()
            time.sleep(0.3)
            driver.quit()
            time.sleep(0.3)
            utils.clicarMicrosiga()
            return robozinho()
        if cont == 20:
            press("enter")
            cont = 0
            
            

    for i, ctrl_imposto in enumerate(indices_e_impostos):
        if ctrl_imposto == 0:
            verificador = operadoresLancamento.verificarValorDoItem(itens, i)
            if verificador == True:
                driver.quit()
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, icmsST_no_item, ipi_no_item = itens[i]
            natureza = operadoresLancamento.copiarNatureza()
            codigo = operadoresLancamento.selecionarCaso(natureza)
            tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
            if tes == True:
                driver.quit()
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
            #SEQUENCIA LOGICA DE LANÇAMENTO SEM IMPOSTO
        elif ctrl_imposto == 1:
            verificador = operadoresLancamento.verificarValorDoItem(itens, i)
            if verificador == True:
                driver.quit()
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, base_e_aliq_icms, icmsST_no_item, ipi_no_item = itens[i]
            bc_icms, aliq_icms = base_e_aliq_icms
            natureza = operadoresLancamento.copiarNatureza()
            codigo = operadoresLancamento.selecionarCaso(natureza)
            tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
            if tes == True:
                driver.quit()
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
            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMS
        elif ctrl_imposto == 2:
            verificador = operadoresLancamento.verificarValorDoItem(itens, i)
            if verificador == True:
                driver.quit()
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, icmsST_no_item, base_e_aliq_ST, ipi_no_item = itens[i]
            base_icms_ST, aliq_icms_ST = base_e_aliq_ST
            natureza = operadoresLancamento.copiarNatureza()
            codigo = operadoresLancamento.selecionarCaso(natureza)
            tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
            if tes == True:
                driver.quit()
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
            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMSST
        elif ctrl_imposto == 3:
            verificador = operadoresLancamento.verificarValorDoItem(itens, i)
            if verificador == True:
                driver.quit()
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, icmsST_no_item, ipi_no_item, base_e_aliq_ipi = itens[i]
            base_ipi, aliq_ipi = base_e_aliq_ipi
            natureza = operadoresLancamento.copiarNatureza()
            codigo = operadoresLancamento.selecionarCaso(natureza)
            tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
            if tes == True:
                driver.quit()
                return robozinho()
            operadoresLancamento.escreverTES(tes)
            if tes in ["406", "421", "423", "102", "403", "411"]:
                operadoresLancamento.zerarImposto()
            operadoresLancamento.inserirDesconto(desc_no_item)
            operadoresLancamento.inserirFrete(frete_no_item)
            operadoresLancamento.inserirSeguro(seg_no_item)
            operadoresLancamento.inserirDespesa(desp_no_item)
            operadoresLancamento.inserirIPI(ipi_no_item, base_ipi, aliq_ipi)
            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA IPI
        elif ctrl_imposto == 4:
            verificador = operadoresLancamento.verificarValorDoItem(itens, i)
            if verificador == True:
                driver.quit()
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, icmsST_no_item, base_e_aliq_ST, ipi_no_item, base_e_aliq_ipi = itens[i]
            base_icms_ST, aliq_icms_ST = base_e_aliq_ST
            base_ipi, aliq_ipi = base_e_aliq_ipi
            natureza = operadoresLancamento.copiarNatureza()
            codigo = operadoresLancamento.selecionarCaso(natureza)
            tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
            if tes == True:
                driver.quit()
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
            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMSST E IPI
        elif ctrl_imposto == 5:
            verificador = operadoresLancamento.verificarValorDoItem(itens, i)
            if verificador == True:
                driver.quit()
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, base_e_aliq_icms, icmsST_no_item, ipi_no_item, base_e_aliq_ipi = itens[i]
            bc_icms, aliq_icms = base_e_aliq_icms
            base_ipi, aliq_ipi = base_e_aliq_ipi
            natureza = operadoresLancamento.copiarNatureza()
            codigo = operadoresLancamento.selecionarCaso(natureza)
            tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
            if tes == True:
                driver.quit()
                return robozinho()
            operadoresLancamento.escreverTES(tes)
            operadoresLancamento.inserirDesconto(desc_no_item)
            operadoresLancamento.inserirFrete(frete_no_item)
            operadoresLancamento.inserirSeguro(seg_no_item)
            operadoresLancamento.inserirDespesa(desp_no_item)
            operadoresLancamento.inserirICMS(icms_no_item, bc_icms, aliq_icms)
            operadoresLancamento.inserirIPI(ipi_no_item, base_ipi, aliq_ipi, passosIPI=3)
            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMS E IPI
        elif ctrl_imposto == 6:
            verificador = operadoresLancamento.verificarValorDoItem(itens, i)
            if verificador == True:
                driver.quit()
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, base_e_aliq_icms, icmsST_no_item, base_e_aliq_ST, ipi_no_item = itens[i]
            bc_icms, aliq_icms = base_e_aliq_icms
            base_icms_ST, aliq_icms_ST = base_e_aliq_ST
            natureza = operadoresLancamento.copiarNatureza()
            codigo = operadoresLancamento.selecionarCaso(natureza)
            tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
            if tes == True:
                driver.quit()
                return robozinho()
            operadoresLancamento.escreverTES(tes)
            operadoresLancamento.inserirDesconto(desc_no_item)
            operadoresLancamento.inserirFrete(frete_no_item)
            operadoresLancamento.inserirSeguro(seg_no_item)
            operadoresLancamento.inserirDespesa(desp_no_item)
            operadoresLancamento.inserirICMS(icms_no_item, bc_icms, aliq_icms)
            operadoresLancamento.inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST, passosST=0)
            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMS E ICMSST
        elif ctrl_imposto == 7:
            verificador = operadoresLancamento.verificarValorDoItem(itens, i)
            if verificador == True:
                driver.quit()
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, frete_no_item, seg_no_item, desp_no_item, icms_no_item, base_e_aliq_icms, icmsST_no_item, base_e_aliq_ST, ipi_no_item, base_e_aliq_ipi = itens[i]
            bc_icms, aliq_icms = base_e_aliq_icms
            base_icms_ST, aliq_icms_ST = base_e_aliq_ST
            base_ipi, aliq_ipi = base_e_aliq_ipi
            natureza = operadoresLancamento.copiarNatureza()
            codigo = operadoresLancamento.selecionarCaso(natureza)
            tes = operadoresLancamento.definirTES(codigo, ctrl_imposto)
            if tes == True:
                driver.quit()
                return robozinho()
            operadoresLancamento.escreverTES(tes)
            operadoresLancamento.inserirDesconto(desc_no_item)
            operadoresLancamento.inserirFrete(frete_no_item)
            operadoresLancamento.inserirSeguro(seg_no_item)
            operadoresLancamento.inserirDespesa(desp_no_item)
            operadoresLancamento.inserirICMS(icms_no_item, bc_icms, aliq_icms)
            operadoresLancamento.inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST, passosST=0)
            operadoresLancamento.inserirIPI(ipi_no_item, base_ipi, aliq_ipi, passosIPI=12)
            #SEQUENCIA LOGICA DE LANÇAMENTO PARA TODOS OS IMPOSTOS

        if len(indices_e_impostos) > 1:
            press("down")
        if i+1 == len(indices_e_impostos):
            press("up")
        time.sleep(1)


    aba_duplicatas = utils.encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\AbaDuplicatas.png')
    x, y =  aba_duplicatas
    mouseClique(x,y, clicks=4, interval=0.1)
    time.sleep(0.6)
    lista_parc = []
    valor_parcela = utils.encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\clicarParcela.png')
    while type(valor_parcela) != tuple:
        moveTo(180, 200)
        mouseClique(x,y, clicks=4, interval=0.1)
        valor_parcela = utils.encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\clicarParcela.png')
        time.sleep(0.4)
    x, y = valor_parcela
    mouseClique(x,y)
    time.sleep(0.5)
    hotkey("ctrl", "c", interval=0.2)
    valor_parcela = pyperclip.paste()
    valor_parcela = utils.formatador4(valor_parcela)
    if valor_parcela != valor_total_da_nf:
        lista_parc.append(valor_parcela)
        while sum(lista_parc) < valor_total_da_nf:
            utils.descerECopiar()
            valor_parcela = pyperclip.paste()
            valor_parcela = utils.formatador4(valor_parcela)
            lista_parc.append(valor_parcela)
        diferenca_NF_siga = sum(lista_parc) - valor_total_da_nf
        if sum(lista_parc) != valor_total_da_nf:
            if diferenca_NF_siga > 10:
                parcela_duplicada = lista_parc.pop()
            diferenca_NF_siga = valor_total_da_nf - sum(lista_parc) 
            ultima_parcela = parcela_duplicada + diferenca_NF_siga
            ultima_parcela = "{:.2f}".format(ultima_parcela)
            ultima_parcela = str(ultima_parcela)  
            mouseClique(x,y)
            descida = len(lista_parc) - 1
            press(["down"]*descida)
            time.sleep(0.4)
            write(ultima_parcela, interval=0.03)
        time.sleep(1)
    while True:
        natureza_duplicata_clique = utils.encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\naturezaDuplicata.png')
        if type(natureza_duplicata_clique) != tuple:
            moveTo(150, 250)
            mouseClique(x,y, clicks=4, interval=0.1)
            time.sleep(0.3)
        else:
            break
    x, y = natureza_duplicata_clique
    mouseClique(x,y)
    time.sleep(0.3)
    hotkey("ctrl", "c", interval=0.2)
    natureza_perc = pyperclip.paste() 
    if natureza_perc != "0,00":
        lista_perc = []
        while sum(lista_perc) < 100.0:
            natureza_perc = utils.formatador3(natureza_perc)
            lista_perc.append(natureza_perc)
            utils.descerECopiar()
            natureza_perc = pyperclip.paste() 
        maior_perc = max(lista_perc)
        natureza_duplicata_clique = utils.encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\naturezaDuplicata.png')
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


    salvar = utils.encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\salvarLancamento.png')
    salvarx, salvary = salvar
    time.sleep(0.7)
    mouseClique(salvarx,salvary, clicks=2, interval=0.1)
    time.sleep(2)
    cont = 0
    while True:
        salvar = utils.encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\salvarLancamento.png')
        if type(salvar) == tuple:
            mouseClique(salvarx,salvary, clicks=2, interval=0.1)
            cont += 1
            time.sleep(1)
            if cont == 2:
                break
        else:
            break
    erro_de_serie = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\ErroDeSerie.png')
    if type(erro_de_serie) == pyscreeze.Box:
        press("enter", interval=0.2) 
        espec_doc = utils.encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\CorrigirErroDeSerie.png')
        x, y = espec_doc
        time.sleep(0.5)
        mouseClique(x,y, clicks=2)
        write("NF", interval=0.1)
        press("enter")
        time.sleep(0.5)
        mouseClique(salvarx,salvary, clicks=2)
    erro_esquisito = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\erroEsquisito.png')
    if type(erro_esquisito) == pyscreeze.Box:
        press("esc")
        quit()
    erro_quantidade = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\erroDeQuantidade.png')
    if type(erro_quantidade) == pyscreeze.Box:
        press("enter")
        utils.cancelarLancamento()
        mudar_a_selecao = utils.encontrarImagemLocalizada(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\mudarASelecao.png')
        x, y = mudar_a_selecao
        mouseClique(x,y, clicks=2)
        driver.quit() 
        time.sleep(0.3)
        utils.clicarMicrosiga()
        return robozinho()

    cont = 0
    etapa_final = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\etapaFinal.png')
    while type(etapa_final) != pyscreeze.Box:
        time.sleep(0.2)
        etapa_final = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\etapaFinal.png')
    press(["tab"]*3, interval=0.9)
    press("enter")
    time.sleep(1.5)
    ultimo_enter = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\finalizarLancamento.png')
    if type(ultimo_enter) != pyscreeze.Box:
        while type(ultimo_enter) != pyscreeze.Box:
            time.sleep(0.2)
            ultimo_enter = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\finalizarLancamento.png')
            cont +=1
            if cont == 10:
                press("enter")
                cont = 0
    press("tab", interval=0.9)
    press("enter")
    time.sleep(1.5)
    aux = False
    while True:
        ultima_tela = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\ultimaTela.png')
        if type(ultima_tela) == pyscreeze.Box:
            aux = True
            while type(ultima_tela) == pyscreeze.Box:
                ultima_tela = utils.encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\ultimaTela.png')
                time.sleep(0.2)
        if aux == True:
            break
        else:
            cont +=1
            time.sleep(0.2)
            if cont == 10:
                press("enter")
                cont = 0

    hotkey("win", "d")
    time.sleep(0.2)
    driver.quit()
    time.sleep(0.2)
    
    return robozinho()


if __name__ == "__main__":
    robozinho()

    



        
