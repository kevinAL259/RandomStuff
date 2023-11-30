import os
import glob
from PyPDF2 import PdfReader, PdfWriter


#NO FURULA
#NO FURULA
#NO FURULA
#NO FURULA
#NO FURULA
#NO FURULA
#NO FURULA

#No les pone contraseña


#Aqui le pondremos la carpeta a la que queremos ponerle pw a los pdf.
Dir = r"C:.\EncriptarPDF"
patron = ".pdf"
Archivos_pdf = glob.glob(os.path.join(Dir, patron))

for Archivos_pdf in Archivos_pdf:
    lector = PdfReader(Archivos_pdf)
    escritor = PdfWriter()

    for page in lector.pages:
        escritor.add_page(page)

#aqui le pondremos la contraseña que queremos que se agregue
    escritor.encrypt("P4ssw0rd246")

    with open(Archivos_pdf, "wb") as f:
        escritor.write(f)

print("Fin")