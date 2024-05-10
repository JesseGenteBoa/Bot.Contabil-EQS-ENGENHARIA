import utils


class ProcessadorXML:
    def __init__(self, doc, cnpj_dict):
        self.doc = doc
        self.cnpj_dict = cnpj_dict
        self.valores_do_item = []

    def processarTotaisNotaFiscal(self):
        totais_nota_fiscal = self.doc["nfeProc"]["NFe"]["infNFe"]["total"]["ICMSTot"]

        teremos_frete = totais_nota_fiscal["vFrete"]
        teremos_frete = utils.formatador(teremos_frete)

        teremos_despesas_acessorias = totais_nota_fiscal["vOutro"]
        teremos_despesas_acessorias = utils.formatador(teremos_despesas_acessorias)

        valor_total_da_nf = totais_nota_fiscal["vNF"]
        valor_total_da_nf = float(valor_total_da_nf)
        valor_total_da_nf = "{:.2f}".format(valor_total_da_nf)

        cnpj_filial_de_entrega = self.doc["nfeProc"]["NFe"]["infNFe"]["dest"]["CNPJ"]
        filial_xml = self.cnpj_dict[cnpj_filial_de_entrega]

        return teremos_frete, teremos_despesas_acessorias, valor_total_da_nf, filial_xml

    def coletarDadosXML(self, coletor_xml, impostos_xml):
        valor_prod = coletor_xml["vProd"] 
        quantidade_comprada = coletor_xml["qCom"]
        quantidade_comprada = utils.formatador(quantidade_comprada, casas_decimais="{:.6f}")
        valor_unitario = coletor_xml["vUnCom"]
        valor_unitario = utils.formatador(valor_unitario, casas_decimais="{:.6f}")
        self.valores_do_item.append(valor_prod)
        self.valores_do_item.append(quantidade_comprada)
        self.valores_do_item.append(valor_unitario)

        try:
            valor_desconto_xml = coletor_xml["vDesc"]
        except KeyError:
            valor_desconto_xml = "0.00"

        self.valores_do_item.append(valor_desconto_xml)

        try:
            busca_icms_xml = impostos_xml["ICMS"]
            atributos_icms = busca_icms_xml.values()
            atributos_icms = list(atributos_icms)
            descompactar_lista = atributos_icms[0]
            valor_icms = descompactar_lista["vICMS"]
        except KeyError:
            valor_icms = "0.00"

        self.valores_do_item.append(valor_icms)

        if valor_icms != "0.00":
            aliquota_icms = descompactar_lista["pICMS"]
            aliquota_icms = utils.formatador2(aliquota_icms)
            bc_icms = descompactar_lista["vBC"]
            self.valores_do_item.append((bc_icms, aliquota_icms))

        try:
            busca_icms_xml = impostos_xml["ICMS"]
            atributos_icms = busca_icms_xml.values()
            atributos_icms = list(atributos_icms)
            descompactar_lista = atributos_icms[0]
            valor_icms_st = descompactar_lista["vICMSST"]
        except KeyError:
            valor_icms_st = "0.00"

        self.valores_do_item.append(valor_icms_st)

        if valor_icms_st != "0.00":
            aliquota_icms_st = descompactar_lista["pICMSST"]
            aliquota_icms_st = utils.formatador2(aliquota_icms_st)
            bc_icms_st = descompactar_lista["vBCST"]
            self.valores_do_item.append((bc_icms_st, aliquota_icms_st))

        try:
            busca_ipi_xml = impostos_xml["IPI"]["IPITrib"]
            valor_ipi = busca_ipi_xml["vIPI"]
            valor_ipi = utils.formatador2(valor_ipi)
        except KeyError:
            valor_ipi = "0.00"

        self.valores_do_item.append(valor_ipi)

        if valor_ipi != "0.00":
            aliquota_ipi = busca_ipi_xml["pIPI"]
            aliquota_ipi = utils.formatador2(aliquota_ipi)
            bc_ipi = busca_ipi_xml["vBC"]
            self.valores_do_item.append((bc_ipi, aliquota_ipi))

        return self.valores_do_item




