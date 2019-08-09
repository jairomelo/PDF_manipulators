import extrac
import PyPDF2

problematic_file = ""

try:
    print(extrac.pdftexto(problematic_file))
except KeyError:
    raise
except PyPDF2.utils.PdfReadError:
    raise
except NotImplementedError:
    raise