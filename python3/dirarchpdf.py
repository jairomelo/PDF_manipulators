import os

try:
    from scandir import walk
except ImportError:
    walk = os.walk


class Dir:

    def __init__(self, directorio, fecha_inicial="0", fecha_final="10000"):
        self.directorio = directorio
        self.fecha_inicial = int(fecha_inicial) - 1
        self.fecha_final = int(fecha_final) + 1
        self.lista = range(self.fecha_inicial, self.fecha_final)

    def buspdfarc(self):

        pdff = []

        for r, d, f in walk(self.directorio):
            for file in f:
                if '.pdf' in file:
                    for i in range(len(self.lista)):
                        fecha = self.lista[i]
                        fechas = str(fecha)
                        if file.find(fechas) != -1:
                            pdff.append(os.path.join(r, file))
        return pdff

    def buspdfall(self):

        pdff = []

        for r, d, f in walk(self.directorio):
            for file in f:
                if '.pdf' in file:
                    pdff.append(os.path.join(r, file))

        return pdff

    def buspdfdir(self):

        pdff = []

        with os.scandir(self.directorio) as archivs:
            for nombre in archivs:
                for i in range(len(self.lista)):
                    fecha = self.lista[i]
                    fechas = str(fecha)
                    if nombre.name.find(fechas) != -1:
                        if nombre.is_dir():
                            pdff.append(nombre.name)

        return pdff
