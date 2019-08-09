import re

import PyPDF2


# Esta función regresa el texto completo de cada página.

def pdftexto(pdfobjec):
    """ pdfobjec: el archivo pdf. """
    pdfread = PyPDF2.PdfFileReader(pdfobjec)
    paginacion = pdfread.numPages
    pagilist = []
    for paginas in range(paginacion):
        paginobj = pdfread.getPage(paginas)
        retorno = paginobj.extractText()
        pagilist.append(retorno)
    pdfobjec.close()
    pgstring = str(pagilist)
    rawstring = pgstring.replace('[\'', '').replace('\']', ',').replace('\'', '')
    return rawstring


# Esta función hace una búsqueda en un pdf determinado

def pdfbusq(pdfobjec, busquery):
    """ pdfobjec: el archivo pdf :: busquery: la cadena de búsqueda. """
    pdfread = PyPDF2.PdfFileReader(pdfobjec)
    paginacion = pdfread.numPages
    cadena = busquery
    resultad = []
    for i in range(paginacion):
        pag_obj = pdfread.getPage(i)
        texto = pag_obj.extractText()
        print("\r" + "Leyendo página " + str(i+1) + ".", end="")
        buscando = re.findall(cadena, texto)
        if not buscando:
            pass
        else:
            resultad.append("Se encontró " + str(buscando) + " en la página núm. " + str(i+1))
    pdfobjec.close()

    return resultad
