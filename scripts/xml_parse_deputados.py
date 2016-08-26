# -*- coding: utf-8
import xml.etree.ElementTree as ET
import csv

csv_arquivo = '../data/AnoAtual.xml.csv'
xml_arquivo = '../data/AnoAtual.xml'
tree = ET.parse(xml_arquivo)
root = tree.getroot()
root = root[0]
header_row = ["txNomeParlamentar","ideCadastro","nuCarteiraParlamentar",\
              "nuLegislatura","sgUF","sgPartido","codLegislatura",\
              "numSubCota","txtDescricao","numEspecificacaoSubCota",\
              "txtDescricaoEspecificacao", "txtFornecedor","txtCNPJCPF",\
              "txtNumero","indTipoDocumento","datEmissao", "vlrDocumento",\
              "vlrGlosa","vlrLiquido","numMes","numAno","numParcela",\
              "txtPassageiro","txtTrecho","numLote","numRessarcimento",\
              "vlrRestituicao", "nuDeputadoId"]
header = False
with open(csv_arquivo, 'w+') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in root:
        complete_row = []
        for value in row:
            try:
                complete_row.append(value.text.encode('utf-8'))
            except:
                try:
                    complete_row.append(value.text)
                except:
                    print "Coulnd't write value", value
                    pass
        if header is False:
            csv_writer.writerow(header_row)
            csv_writer.writerow(complete_row)
            header = True
        else:
            csv_writer.writerow(complete_row)
        print "Linha", counter, "salva com sucesso!"
    csv_file.close()
