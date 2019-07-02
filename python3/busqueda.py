#!/usr/bin/python
# -*- coding: utf-8 -*-

import errno
import os
import re
import sys
from time import strftime

import PyPDF2

import dirarchpdf
import extrac

error_log = open("error_log.txt", "a")

carp = input("¿En qué carpeta desea hacer la búsqueda? ")

rdf = input("Buscar en todo [1] o en un rango de fechas [2]: ")

if rdf == "2":
    fecha_init = input("Fecha inicial: ")
    fecha_fina = input("Fecha final: ")
    busqueda = dirarchpdf.Dir(carp, fecha_init, fecha_fina)
else:
    busqueda = dirarchpdf.Dir(carp)

pdb = input("Ingrese su búsqueda: ")

rutas = dirarchpdf.Dir.buspdfall(busqueda)

print("Se realizará la búsqueda en los siguientes {} archivos: ".format(len(rutas)))
print(dirarchpdf.Dir.buspdfall(busqueda))

try:
    os.makedirs("resultados")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

try:
    resultado = open("resultados/{}.txt".format(pdb), "a")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

print("Buscando archivos pdf en el directorio indicado...")

resultado.write(strftime("%d %b %Y %H:%M"))

for nomarc in rutas:
    nomarch = nomarc.lstrip()
    open(nomarch, 'rb')
    print("Leyendo: " + nomarch)
    mipdf = open(nomarch, 'rb')
    buscar = re.compile(pdb, flags=re.IGNORECASE)
    try:
        caja_busq = extrac.pdfbusq(mipdf, buscar)
        if len(caja_busq) > 1:
            resultado.write(
                "\n Se encontraron {} resultados en {} \n {}".format(len(caja_busq) - 1, nomarch, str(caja_busq)))
            print(caja_busq)
        else:
            print("Sin resultados")
    except KeyError:
        error_log.write(
            "\n# [{}] No se pudo leer el archivo {}. Error: {} \n".format(strftime("%d %b %Y %H:%M"), nomarch,
                                                                          sys.exc_info()[0]))
        pass
    except PyPDF2.utils.PdfReadError:
        error_log.write(
            "\n# [{}] No se pudo leer el archivo {}. Error: {} \n".format(strftime("%d %b %Y %H:%M"), nomarch,
                                                                          sys.exc_info()[0]))
        pass
    except NotImplementedError:
        error_log.write(
            "\n# [{}] No se pudo leer el archivo {}. Error: {} \n".format(strftime("%d %b %Y %H:%M"), nomarch,
                                                                          sys.exc_info()[0]))
        pass

resultado.close()
error_log.close()

print("Finalizó la búsqueda :)")
print("El archivo está guardado en {}".format(os.getcwd()))
