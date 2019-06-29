import PyPDF2
import re

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
    resultad.append("Este es el resultado de la búsqueda \"{}\" en el archivo {}".format(busquery, pdfobjec))
    for i in range(paginacion):
        pag_obj = pdfread.getPage(i)
        texto = pag_obj.extractText()
        print("\r" + "Leyendo página " + str(i) + ".", end="")
        buscando = re.findall(cadena, texto)
        if not buscando:
            pass
        else:
            resultad.append("Se encontró " + str(buscando) + " en la página núm. " + str(i))
    pdfobjec.close()

    return resultad