''' Emissor de certificados em pdf automático
que imprime o certificado em pdf contendo
o nome da pessoa e o curso que ela está sendo certificada
com base nos dados de uma tabela em excel
 1- importar dados
 2- preparar pdf
 3-imprimir os certificados de todos da lista
  '''
'''importar bibliotecas'''
import pandas as pd #carregar bibli pandas
from fpdf import FPDF

'''importar e verificar  dados'''

dados = pd.read_excel("dados_alunos.xlsx")
print(dados.info())#verificar os dados
print(dados)

'''preencher e imprimir os certificados'''
  # criar arquivo

for i in range(len(dados)):#laço de repetição para emitir os diferentes certificados enquanto houver dados na tabela 
    nome = dados.loc[i, 'nome']
    curso = dados.loc[i, 'curso']
    '''preparar o pdf'''
    pdf = FPDF()
    pdf.set_font("Arial", size=18)  # selecionar uma fonte para o texto
    pdf.add_page(orientation='L')  # add uma pagina com orientação de paissagem e formato papel A4
    pdf.image("template_certificado.png", x=0, y=0)  # utilizar uma base predefinida "template" para o pdf
    pdf.text(70, 100, nome)  # add um texto nas cordeenadas x e y
    pdf.text(70, 122, curso)
    pdf.output(f"Certificado {nome}.pdf")  # criar arquivo pdf



