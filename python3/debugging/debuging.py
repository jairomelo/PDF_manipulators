import extrac
import PyPDF2

problematic_file = "E:/experiments/buscar_recolectar/python3/test_files/pf/encrypted_np.pdf"

try:
    print(extrac.pdftexto(problematic_file))
except KeyError:
    raise
except PyPDF2.utils.PdfReadError:
    raise
except NotImplementedError:
    raise