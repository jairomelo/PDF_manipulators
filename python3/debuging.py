import PyPDF2
import sys


def debug(pdf):
    pdfread = PyPDF2.PdfFileReader(pdf)
    pdfread.getNumPages()
    print("Sin problemas :D ")


problematic_file = "E:\\Biblioteca\\Raros y Manuscritos\\Cultura, Arte, Música, Literatura\\[1528] Juan de Mena - las CCC [glosadas por Núñez de Toledo].pdf"

try:
    debug(problematic_file)
except:
    print("No se pudo leer el archivo. Error: ", sys.exc_info()[0])
    raise
