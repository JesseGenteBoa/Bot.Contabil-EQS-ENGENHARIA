import pyautogui        
import pyperclip        
import time
import xmltodict   
import pyscreeze
from selenium import webdriver                         
from selenium.webdriver.common.by import By

pyautogui.FAILSAFE = True   


processos_ja_vistos = []

cnpj_dict = {'80464753000197': '02', '80464753000430': '04', '80464753000510': '05', '80464753000782': '07', '80464753000863': '08', '80464753000944': '09', '80464753001088': '10', '80464753001169': '11', '80464753001240': '12', '80464753001320': '13', '80464753001401': '14', '80464753001592': '15', '80464753001673': '16', '80464753001916': '19', '80464753002050': '20', '80464753002130': '21', '80464753002211': '22', '80464753002564': '25', '80464753002645': '26', '80464753002807': '28', '80464753002998': '29', '80464753003021': '30', '80464753003102': '31', '80464753003293': '32', '80464753003374': '33', '80464753003617': '34', '80464753003536': '35', '80464753003455': '36', '80464753003706': '37', '80464753003960': '39', '80464753004001': '40', '80464753004184': '41', '80464753004265': '42', '80464753004346': '43', '80464753004699': '46', '80464753004770': '47', '80464753004850': '48', '80464753004931': '49', '80464753005075': '50', '80464753005156': '51', '80464753005407': '54', '80464753005580': '55', '80464753005660': '56', '80464753005741': '57', '80464753005822': '58', '80464753005903': '59', '80464753006047': '60'}


def encontrarImagem(imagem):
    cont = 0
    while True:
        try:
            encontrou = pyautogui.locateOnScreen(imagem, grayscale=True, confidence = 0.8)
            return encontrou
        except pyautogui.ImageNotFoundException:
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
            x, y = pyautogui.locateCenterOnScreen(imagem, grayscale=True, confidence=0.99)
            return (x, y)
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            cont += 1
            if cont == 3:
                break
            print("Imagem não encontrada")
            pass


def clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsiga.png'):
    clique = encontrarImagemLocalizada(imagem)
    pyautogui.click(clique)

def voltarEDescer(passos=1):
    pyautogui.hotkey(["shift", "tab"]*passos, interval=0.15)
    pyautogui.press("down")

def reiniciarPortal():
    clicarMicrosiga()
    voltarEDescer(passos=3)
    

def robozinho():
    clicarMicrosiga()
    time.sleep(1)
    clicar2 = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\verDocumentos.png')
    time.sleep(0.5)
    pyautogui.click(clicar2, clicks=2)
    time.sleep(1)        
    pyautogui.hotkey("alt", "d", interval=0.1)  
    pyautogui.hotkey("ctrl", "c")
    link = pyperclip.paste()
    options = webdriver.ChromeOptions()
    options.add_argument(r'user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data\Perfil Selenium')
    driver = webdriver.Chrome(options=options)
    time.sleep(0.5)
    driver.get(link)
    time.sleep(2)
    tempo_max = 0
    pyautogui.FAILSAFE = True  

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
                        pyautogui.hotkey("alt", "tab", interval=0.05)
                        pyautogui.hotkey("ctrl", "w")
                        reiniciarPortal()
                        driver.quit()
                        clicarMicrosiga()
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
                                reiniciarPortal()
                                driver.quit()
                                time.sleep(0.5)
                                clicarMicrosiga()
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
            pyautogui.press(["enter"])
        if tempo_max == 40:
            reiniciarPortal()
            driver.quit()
            clicarMicrosiga()
            return robozinho()
        

    pyautogui.hotkey("alt", "tab", interval=0.05)
    pyautogui.hotkey("ctrl", "w")


    caminho = "C:\\Users\\User\\OneDrive - EQS Engenharia Ltda\\Documentos\\GitHub\\GitHubDoJessezinho\\mark3\\xmlFiscalio\\" + chave_de_acesso + ".xml"

    try:
        with open(caminho) as fd:
            doc = xmltodict.parse(fd.read())
    except:
        driver.quit()
        exportarXML = encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\exportarXML.png')
        time.sleep(1)
        pyautogui.click(exportarXML, clicks=4, interval=0.07)
        time.sleep(2)
        clicar_servidor = encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\clicarServidor.png')
        pyautogui.click(clicar_servidor, clicks=3, interval=0.07)
        pyperclip.copy("C:\\Users\\User\\OneDrive - EQS Engenharia Ltda\\Documentos\\GitHub\\GitHubDoJessezinho\\mark3\\xmlFiscalio\\")
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press(["tab"]*6, interval=0.5)
        pyautogui.press("enter")
        time.sleep(1.5)
        pyautogui.press("enter")
        time.sleep(1.5)
        pyautogui.press("enter")
        time.sleep(3)
        caminho = "C:\\Users\\User\\OneDrive - EQS Engenharia Ltda\\Documentos\\GitHub\\GitHubDoJessezinho\\mark3\\xmlFiscalio\\" + chave_de_acesso + ".xml"
        auxiliar = False
        try:
            with open(caminho) as fd:
                doc = xmltodict.parse(fd.read())
        except:
            auxiliar = True
        if auxiliar == True:
            pyautogui.hotkey(["tab"]*3, interval=0.1)
            pyautogui.press("down")
            driver.quit()
            clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsigaSelecionado.png')
            return robozinho()
        else:
            time.sleep(1.2)
            clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsigaSelecionado.png')
            time.sleep(0.5)

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

    totais_nota_fiscal = doc["nfeProc"]["NFe"]["infNFe"]["total"]["ICMSTot"]
    teremos_frete = totais_nota_fiscal["vFrete"]
    teremos_frete = formatador(teremos_frete)
    teremos_despesas_acessorias = totais_nota_fiscal["vOutro"]
    teremos_despesas_acessorias = formatador(teremos_despesas_acessorias)
    valor_total_da_nf = totais_nota_fiscal["vNF"]
    valor_total_da_nf = float(valor_total_da_nf)
    valor_total_da_nf = "{:.2f}".format(valor_total_da_nf)

    cnpj_filial_de_entrega = doc["nfeProc"]["NFe"]["infNFe"]["dest"]["CNPJ"]
    filial_xml = cnpj_dict[cnpj_filial_de_entrega]

    valores_do_item = []

    def coletarDadosXML():
        valor_prod = coletor_xml["vProd"] 
        quantidade_comprada = coletor_xml["qCom"]
        quantidade_comprada = formatador(quantidade_comprada, casas_decimais="{:.6f}")
        valor_unitario = coletor_xml["vUnCom"]
        valor_unitario = formatador(valor_unitario, casas_decimais="{:.6f}")
        valores_do_item.append(valor_prod)
        valores_do_item.append(quantidade_comprada)
        valores_do_item.append(valor_unitario)

        try:
            valor_desconto_xml = coletor_xml["vDesc"]
        except KeyError:
            valor_desconto_xml = "0.00"

        valores_do_item.append(valor_desconto_xml)

        try:
            busca_icms_xml = impostos_xml["ICMS"]
            atributos_icms = busca_icms_xml.values()
            atributos_icms = list(atributos_icms)
            descompactar_lista = atributos_icms[0]
            valor_icms = descompactar_lista["vICMS"]
        except KeyError:
            valor_icms = "0.00"

        valores_do_item.append(valor_icms)

        if valor_icms != "0.00":
            aliquota_icms = descompactar_lista["pICMS"]
            aliquota_icms = formatador2(aliquota_icms)
            bc_icms = descompactar_lista["vBC"]
            valores_do_item.append((bc_icms, aliquota_icms))

        try:
            busca_icms_xml = impostos_xml["ICMS"]
            atributos_icms = busca_icms_xml.values()
            atributos_icms = list(atributos_icms)
            descompactar_lista = atributos_icms[0]
            valor_icms_st = descompactar_lista["vICMSST"]
        except KeyError:
            valor_icms_st = "0.00"

        valores_do_item.append(valor_icms_st)

        if valor_icms_st != "0.00":
            aliquota_icms_st = descompactar_lista["pICMSST"]
            aliquota_icms_st = formatador2(aliquota_icms_st)
            bc_icms_st = descompactar_lista["vBCST"]
            valores_do_item.append((bc_icms_st, aliquota_icms_st))

        try:
            busca_ipi_xml = impostos_xml["IPI"]["IPITrib"]
            valor_ipi = busca_ipi_xml["vIPI"]
            valor_ipi = formatador2(valor_ipi)
        except KeyError:
            valor_ipi = "0.00"

        valores_do_item.append(valor_ipi)

        if valor_ipi != "0.00":
            aliquota_ipi = busca_ipi_xml["pIPI"]
            aliquota_ipi = formatador2(aliquota_ipi)
            bc_ipi = busca_ipi_xml["vBC"]
            valores_do_item.append((bc_ipi, aliquota_ipi))

        return valores_do_item


    const_item = 0
    while True:
        try:
            coletor_xml = doc["nfeProc"]["NFe"]["infNFe"]["det"]["prod"]
            impostos_xml = doc["nfeProc"]["NFe"]["infNFe"]["det"]["imposto"]
            coletarDadosXML()
            break
        except TypeError:
            try:
                coletor_xml = doc["nfeProc"]["NFe"]["infNFe"]["det"][const_item]["prod"]
                impostos_xml = doc["nfeProc"]["NFe"]["infNFe"]["det"][const_item]["imposto"]
                coletarDadosXML()
                const_item += 1
            except IndexError:
                break
    

    clicarMicrosiga()
    clicar2 = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\DadosDaNota.png')
    pyautogui.click(clicar2, clicks=4, interval=0.1)
    time.sleep(0.5)
    try:
        aparece_click = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\NCMsegue.png')
        if type(aparece_click) == pyscreeze.Box:
            time.sleep(0.5)
            pyautogui.press("enter")
    finally:
        pyautogui.write("408")

    pyautogui.press("tab")
    time.sleep(0.7)
    pyautogui.hotkey("ctrl", "c")
    filial_pedido = pyperclip.paste()
    if filial_pedido == filial_xml:
        pyautogui.press("tab", interval=0.5)
        pyautogui.press("enter")
    else:
        clicar = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\CancelarFilial.png')
        pyautogui.click(clicar, clicks=2, interval=0.07)
        voltarEDescer()
        driver.quit()
        clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsigaSelecionado.png')
        return robozinho()

    try:
        time.sleep(0.5)
        aparece_enter = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\AtencaoEstoque.png')
        if type(aparece_enter) == pyscreeze.Box: 
            pyautogui.press("enter")
        aparece_enter2 = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\TES102.png')
        if type(aparece_enter2) == pyscreeze.Box:
            pyautogui.press("enter") 
            pyautogui.press(["tab"]*2)
            pyautogui.write("102")
            pyautogui.press(["tab"]*2, interval=0.5)
            pyautogui.press("enter") 
    finally:
        pass


    while True:
        time.sleep(1)
        tela_de_lancamento = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\AbriuOProcesso.png')
        if type(tela_de_lancamento) == pyscreeze.Box:
            clicar = encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\clicarValorUnit.png')
            pyautogui.click(clicar)
            break
        
        lancamento_retroativo = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\LancamentoRetroativo.png')
        nota_ja_lancada = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\ProcessoJaLancado.png')
        fornecedor_bloqueado = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\FornecedorBloqueado.png')
        if type(lancamento_retroativo) == pyscreeze.Box or type(nota_ja_lancada) == pyscreeze.Box or type(fornecedor_bloqueado) == pyscreeze.Box:
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)

        erro_generico = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\ErroGenerico.png')
        if type(erro_generico) == pyscreeze.Box:
            time.sleep(1)
            pyautogui.press("enter", interval=2) 
            pyautogui.press("esc", interval=2) 
            pyautogui.press("enter", interval=2)    
            voltarEDescer()
            driver.quit()
            time.sleep(1)
            clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsigaSelecionado.png')
            return robozinho()
        
        chave_nao_encontrada = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\chaveNaoEncontradaNoSefaz.png')
        if type(chave_nao_encontrada) == pyscreeze.Box:
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            clicar2 = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\CancelarLancamento.png')
            while type(clicar2) != pyscreeze.Box:
                clicar2 = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\CancelarLancamento.png') 
                time.sleep(1)
            pyautogui.click(clicar2, clicks=2, interval=0.07)
            time.sleep(2)
            pyautogui.press("esc", interval=1)
            pyautogui.press("enter", interval=1)
            aguarde = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
            while type(aguarde) == pyscreeze.Box:
                aguarde = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
                time.sleep(0.3)
            voltarEDescer()
            driver.quit()
            time.sleep(0.5)
            clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsigaSelecionado.png')
            return robozinho()


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
            encontrar = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\valitenErrado.png')
            if type(encontrar) == pyscreeze.Box:
                pyautogui.press("enter")
                pyautogui.press("esc")
                pyautogui.press(["left"]*5)
                time.sleep(0.2)
                pyautogui.hotkey("ctrl", "c", interval=0.5)
                quantidade_siga = pyperclip.paste()
                if quantidade_siga == lista[indiceX][1]:
                    pyautogui.press("right")
                    pyautogui.write(lista[indiceX][2])
                    pyautogui.press(["right"]*3)
                else:
                    cancelar_lancamento = True
                    clicar2 = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\CancelarLancamento.png')
                    time.sleep(0.5)
                    pyautogui.click(clicar2, clicks=2, interval=0.1)
                    aguarde = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
                    while type(aguarde) == pyscreeze.Box:
                        aguarde = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
                        time.sleep(1)
                    voltarEDescer()
                    driver.quit()
                    clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsigaSelecionado.png')
            else:
                pyautogui.press("left")
        return cancelar_lancamento
    

    controlador = len(valores_do_item)

    itens = []
    indices_e_impostos = []
    cont = 0
    aux = 0
    try:
        while cont <= controlador:
            tem_icms = False
            tem_icms_st = False
            tem_ipi = False
            if valores_do_item[cont+4] != "0.00":
                cont+=5
                tem_icms = True
            else:
                cont+=4
            if valores_do_item[cont+1] != "0.00":
                cont+=3
                tem_icms_st = True
            else:
                cont+=2
            if valores_do_item[cont] != "0.00":
                cont+=2
                tem_ipi = True
            else:
                cont+=1
            itens.append(valores_do_item[aux:cont])
            aux=cont
            if tem_icms == True and tem_icms_st == True and tem_ipi == True:
                ctrl_imposto = 7
            elif tem_icms == True and tem_icms_st == True:
                ctrl_imposto = 6
            elif tem_icms == True and tem_ipi == True:
                ctrl_imposto = 5
            elif tem_icms_st == True and tem_ipi == True:
                ctrl_imposto = 4
            elif tem_ipi == True:
                ctrl_imposto = 3
            elif tem_icms_st == True:
                ctrl_imposto = 2
            elif tem_icms == True:
                ctrl_imposto = 1
            else:
                ctrl_imposto = 0
            indices_e_impostos.append(ctrl_imposto)
    except IndexError:
        pass


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
            clicar2 = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\CancelarLancamento.png')
            time.sleep(0.3)
            pyautogui.click(clicar2)
            aguarde = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
            while type(aguarde) == pyscreeze.Box:
                aguarde = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
                time.sleep(1)
            voltarEDescer()
            driver.quit()
            clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsigaSelecionado.png')
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


    for i, ctrl_imposto in enumerate(indices_e_impostos):
        if ctrl_imposto == 0:
            verificador = verificarValorDoItem(itens, i)
            if verificador == True:
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, icms_no_item, icmsST_no_item, ipi_no_item = itens[i]
            natureza = copiarNatureza()
            codigo = selecionarCaso(natureza)
            tes = definirTES(codigo, ctrl_imposto)
            if tes == True:
                return robozinho()
            escreverTES(tes)
            if tes in ["102", "405", "408"]:
                zerarImposto()
            elif tes in ["406", "421", "423"]:
                zerarImposto()
                zerarImposto(passos_ida=12, passos_volta=13)
            inserirDesconto(desc_no_item)
            #SEQUENCIA LOGICA DE LANÇAMENTO SEM IMPOSTO
        elif ctrl_imposto == 1:
            verificador = verificarValorDoItem(itens, i)
            if verificador == True:
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, icms_no_item, base_e_aliq_icms, icmsST_no_item, ipi_no_item = itens[i]
            bc_icms, aliq_icms = base_e_aliq_icms
            natureza = copiarNatureza()
            codigo = selecionarCaso(natureza)
            tes = definirTES(codigo, ctrl_imposto)
            if tes == True:
                return robozinho()
            escreverTES(tes)
            if tes in ["406", "421", "423"]:
                zerarImposto(passos_ida=12, passos_volta=13)
            inserirDesconto(desc_no_item)
            inserirICMS(icms_no_item, bc_icms, aliq_icms)
            pyautogui.press(["left"]*9)
            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMS
        elif ctrl_imposto == 2:
            verificador = verificarValorDoItem(itens, i)
            if verificador == True:
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, icms_no_item, icmsST_no_item, base_e_aliq_ST, ipi_no_item = itens[i]
            base_icms_ST, aliq_icms_ST = base_e_aliq_ST
            natureza = copiarNatureza()
            codigo = selecionarCaso(natureza)
            tes = definirTES(codigo, ctrl_imposto)
            if tes == True:
                return robozinho()
            escreverTES(tes)
            if tes in ["102", "405", "408"]:
                zerarImposto()
            elif tes in ["406", "421", "423"]:
                zerarImposto()
                zerarImposto(passos_ida=12, passos_volta=13)
            inserirDesconto(desc_no_item)
            inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST)
            pyautogui.press(["left"]*12)
            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMSST
        elif ctrl_imposto == 3:
            verificador = verificarValorDoItem(itens, i)
            if verificador == True:
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, icms_no_item, icmsST_no_item, ipi_no_item, base_e_aliq_ipi = itens[i]
            base_ipi, aliq_ipi = base_e_aliq_ipi
            natureza = copiarNatureza()
            codigo = selecionarCaso(natureza)
            tes = definirTES(codigo, ctrl_imposto)
            if tes == True:
                return robozinho()
            escreverTES(tes)
            if tes in ["406", "421", "423", "102", "403", "411"]:
                zerarImposto()
            inserirDesconto(desc_no_item)
            inserirIPI(ipi_no_item, base_ipi, aliq_ipi)
            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA IPI
        elif ctrl_imposto == 4:
            verificador = verificarValorDoItem(itens, i)
            if verificador == True:
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, icms_no_item, icmsST_no_item, base_e_aliq_ST, ipi_no_item, base_e_aliq_ipi = itens[i]
            base_icms_ST, aliq_icms_ST = base_e_aliq_ST
            base_ipi, aliq_ipi = base_e_aliq_ipi
            natureza = copiarNatureza()
            codigo = selecionarCaso(natureza)
            tes = definirTES(codigo, ctrl_imposto)
            if tes == True:
                return robozinho()
            escreverTES(tes)
            if tes in ["406", "421", "423", "102", "411"]:
                zerarImposto()
            inserirDesconto(desc_no_item)
            inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST)
            inserirIPI(ipi_no_item, base_ipi, aliq_ipi, passosIPI=0)
            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMSST E IPI
        elif ctrl_imposto == 5:
            verificador = verificarValorDoItem(itens, i)
            if verificador == True:
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, icms_no_item, base_e_aliq_icms, icmsST_no_item, ipi_no_item, base_e_aliq_ipi = itens[i]
            bc_icms, aliq_icms = base_e_aliq_icms
            base_ipi, aliq_ipi = base_e_aliq_ipi
            natureza = copiarNatureza()
            codigo = selecionarCaso(natureza)
            tes = definirTES(codigo, ctrl_imposto)
            if tes == True:
                return robozinho()
            escreverTES(tes)
            inserirDesconto(desc_no_item)
            inserirICMS(icms_no_item, bc_icms, aliq_icms)
            inserirIPI(ipi_no_item, base_ipi, aliq_ipi, passosIPI=3)
            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMS E IPI
        elif ctrl_imposto == 6:
            verificador = verificarValorDoItem(itens, i)
            if verificador == True:
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, icms_no_item, base_e_aliq_icms, icmsST_no_item, base_e_aliq_ST, ipi_no_item = itens[i]
            bc_icms, aliq_icms = base_e_aliq_icms
            base_icms_ST, aliq_icms_ST = base_e_aliq_ST
            natureza = copiarNatureza()
            codigo = selecionarCaso(natureza)
            tes = definirTES(codigo, ctrl_imposto)
            if tes == True:
                return robozinho()
            escreverTES(tes)
            inserirDesconto(desc_no_item)
            inserirICMS(icms_no_item, bc_icms, aliq_icms)
            inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST, passosST=0)
            pyautogui.press(["left"]*12)
            #SEQUENCIA LOGICA DE LANÇAMENTO SÓ PARA ICMS E ICMSST
        elif ctrl_imposto == 7:
            verificador = verificarValorDoItem(itens, i)
            if verificador == True:
                return robozinho()
            valor_do_item, quant_do_item, vl_unit_item, desc_no_item, icms_no_item, base_e_aliq_icms, icmsST_no_item, base_e_aliq_ST, ipi_no_item, base_e_aliq_ipi = itens[i]
            bc_icms, aliq_icms = base_e_aliq_icms
            base_icms_ST, aliq_icms_ST = base_e_aliq_ST
            base_ipi, aliq_ipi = base_e_aliq_ipi
            natureza = copiarNatureza()
            codigo = selecionarCaso(natureza)
            tes = definirTES(codigo, ctrl_imposto)
            if tes == True:
                return robozinho()
            escreverTES(tes)
            inserirDesconto(desc_no_item)
            inserirICMS(icms_no_item, bc_icms, aliq_icms)
            inserirICMSST(icmsST_no_item, base_icms_ST, aliq_icms_ST, passosST=0)
            inserirIPI(ipi_no_item, base_ipi, aliq_ipi, passosIPI=0)
            #SEQUENCIA LOGICA DE LANÇAMENTO PARA TODOS OS IMPOSTOS

        if len(indices_e_impostos) > 1:
            pyautogui.press("down")
        if i+1 == len(indices_e_impostos):
            pyautogui.press("up")
        time.sleep(1)


    proxima_etapa = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\AbaDescontos.png')
    time.sleep(1)
    pyautogui.click(proxima_etapa, clicks=4, interval=0.1)
    time.sleep(0.7)
    clicar = encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\ClicarNaAbaDescontos.png')
    x, y = clicar
    pyautogui.click(x, y)
    pyautogui.hotkey(["shift", "tab"]*2, interval=0.09)
    pyautogui.write(teremos_frete, interval=0.07)
    time.sleep(0.7)
    pyautogui.write(teremos_despesas_acessorias, interval=0.07)
    time.sleep(0.7)


    def formatador3(variavel):
        variavel = variavel.replace(",", ".")
        variavel = float(variavel)
        return variavel

    def formatador4(variavel):
        valor_parcela = valor_parcela.replace(".", "")
        formatador3(variavel)
        return variavel
        
    clicar = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\AbaDuplicatas.png')
    pyautogui.click(clicar, clicks=4, interval=0.1)
    time.sleep(0.3)
    clicar2 = encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\naturezaDuplicata.png')
    pyautogui.click(clicar2)
    pyautogui.hotkey("ctrl", "c", interval=0.1)
    natureza_perc = pyperclip.paste() 
    if natureza_perc != "0,00":
        lista_perc = []
        while sum(lista_perc) < 100.0:
            natureza_perc = formatador3(natureza_perc)
            lista_perc.append(natureza_perc)
            pyautogui.press("down", interval=0.1)
            pyautogui.hotkey("ctrl", "c", interval=0.1)
            natureza_perc = pyperclip.paste() 
        maior_perc = max(lista_perc)
        clicar2 = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\naturezaDuplicata.png')
        pyautogui.click(clicar2)
        pyautogui.press("up")
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "c", interval=0.1)
        perc_majoritario = pyperclip.paste()
        perc_majoritario = formatador3(perc_majoritario)
        while perc_majoritario != maior_perc:
            pyautogui.press("down", interval=0.1)
            pyautogui.hotkey("ctrl", "c", interval=0.1)
            perc_majoritario = pyperclip.paste()
            perc_majoritario = formatador3(perc_majoritario)
        pyautogui.press("left")
        pyautogui.hotkey("ctrl", "c", interval=0.1)
        natureza_duplicata = pyperclip.paste()
        pyautogui.hotkey(["shift", "tab"]*5, interval=0.2)
        pyautogui.write(natureza_duplicata)
        pyautogui.press("tab")
        time.sleep(1)


    salvar = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\salvarLancamento.png')
    pyautogui.click(salvar, clicks=2, interval=0.1)
    time.sleep(2)
    erro_de_serie = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\ErroDeSerie.png')
    if type(erro_de_serie) == pyscreeze.Box:
        pyautogui.press("enter", interval=0.2) 
        espec_doc = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\CorrigirErroDeSerie.png')
        pyautogui.click(espec_doc, clicks=2)
        pyautogui.write("NF")
        pyautogui.press("enter")
        pyautogui.click(salvar, clicks=2)
    erro_esquisito = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\erroEsquisito.png')
    if type(erro_esquisito) == pyscreeze.Box:
        pyautogui.press("esc")
        quit()
    erro_quantidade = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\erroDeQuantidade.png')
    if type(erro_quantidade) == pyscreeze.Box:
        pyautogui.press("enter")
        clicar2 = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\CancelarLancamento.png')
        time.sleep(0.3)
        pyautogui.click(clicar2, clicks=2, interval=0.1)
        aguarde = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
        while type(aguarde) == pyscreeze.Box:
            aguarde = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\Aguarde.png') 
            time.sleep(1)
        voltarEDescer()
        driver.quit() 
        clicarMicrosiga()
        return robozinho()
    erro_de_parcela = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\corrigirValorParcela.png')  
    if type(erro_de_parcela) == pyscreeze.Box:
        while type(erro_de_parcela) == pyscreeze.Box:
            pyautogui.press("enter")
            time.sleep(2)
            erro_de_parcela = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\corrigirValorParcela.png')
        lista_parc = []
        valor_parcela = encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\clicarParcela.png')
        pyautogui.click(valor_parcela)
        pyautogui.hotkey("ctrl", "c", interval=0.1)
        valor_parcela = pyperclip.paste()
        valor_parcela = formatador4(valor_parcela)
        lista_parc.append(valor_parcela)
        while sum(lista_parc) < valor_total_da_nf:
            pyautogui.press("down")
            pyautogui.hotkey("ctrl", "c", interval=0.1)
            valor_parcela = pyperclip.paste()
            valor_parcela = formatador4(valor_parcela)
            lista_parc.append(valor_parcela)
        parcela_duplicada = lista_parc.pop()
        diferenca_NF_siga = valor_total_da_nf - sum(lista_parc)
        ultima_parcela = parcela_duplicada + diferenca_NF_siga
        ultima_parcela = "{:.2f}".format(ultima_parcela)
        ultima_parcela = str(ultima_parcela)
        valor_parcela = encontrarImagemLocalizada(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\clicarParcela.png')
        pyautogui.click(valor_parcela)
        descida = len(lista_parc) - 1
        pyautogui.press(["down"]*descida)
        pyautogui.write(ultima_parcela)
        time.sleep(1)
        salvar = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\salvarLancamento.png')
        pyautogui.click(salvar, clicks=2, interval=0.1)


    etapa_final = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\etapaFinal.png')
    while type(etapa_final) != pyscreeze.Box:
        time.sleep(0.2)
        etapa_final = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\etapaFinal.png')
    pyautogui.press(["tab"]*3, interval=0.9)
    pyautogui.press("enter")
    time.sleep(1)
    ultimo_click = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\finalizarLancamento.png')
    if type(ultimo_click) != pyscreeze.Box:
        while type(ultimo_click) != pyscreeze.Box:
            time.sleep(0.2)
            ultimo_click = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\finalizarLancamento.png')
    pyautogui.press("tab", interval=0.9)
    pyautogui.press("enter")
    time.sleep(1)
    ultima_tela = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\ultimaTela.png')
    while type(ultima_tela) == pyscreeze.Box:
        time.sleep(0.2)
        ultima_tela = encontrarImagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\ultimaTela.png')

    driver.quit()
             
    clicarMicrosiga(imagem=r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsigaSelecionado.png')
    
    return robozinho()


if __name__ == "__main__":
    robozinho()

    



        
