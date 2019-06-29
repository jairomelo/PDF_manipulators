import re
import os
import sys

import dirarchpdf
import extrac

rdf = input("Buscar en todo [1] o en un rango de fechas [2]: ")

if rdf == "2":
    fecha_init = input("Fecha inicial: ")
    fecha_fina = input("Fecha final: ")
else:
    fecha_init = "0"
    fecha_fina = "10000"

carp = input("¿En qué carpeta desea hacer la búsqueda? ")

pdb = input("Ingrese su búsqueda: ")

busqueda = dirarchpdf.Dir(carp, fecha_init, fecha_fina)

rutas = dirarchpdf.Dir.buspdfall(busqueda)

print("Se realizará la búsqueda en los siguientes {} archivos: ".format(len(rutas)))
print(dirarchpdf.Dir.buspdfall(busqueda))

try:
    os.makedirs("resultados")
except OSError as error:
    if error.errno != errno.EEXIST:
        pass

if not os.path.exists("resultados/{}.txt".format(pdb)):
    resultado = open("resultados/{}.txt".format(pdb), "a")
else:
    pdbb = input("¿Cómo quiere llamar al archivo de resultados?: ")
    resultado = open("resultados/{}.txt".format(pdbb), "a")


print("Buscando archivos pdf en el directorio indicado...")

for nomarc in rutas:
    nomarch = nomarc.lstrip()
    open(nomarch, 'rb')
    print("Leyendo: " + nomarch)
    mipdf = open(nomarch, 'rb')
    buscar = re.compile(pdb, flags=re.IGNORECASE)
    try:
        caja_busq = extrac.pdfbusq(mipdf, buscar)
        if len(caja_busq) > 1:
            resultado.write("Se encontraron {} resultados en {}".format(len(caja_busq), nomarch) + "\n" + str(caja_busq))
            print(caja_busq)
        else:
            print("Sin resultados")
    except:
        print("No se pudo leer el archivo. Error:", sys.exc_info()[0])
        pass

resultado.close()

print("Finalizó la búsqueda :)")
print("El archivo está guardado en {}".format(os.getcwd()))