import PyPDF2

PDF_Password = PyPDF2.PdfReader('olamundo.pdf')
with open('passwords.txt','r',encoding='utf8') as f:
    for line in f:
        Password = line.strip()
        if PDF_Password.decrypt(Password) !=0:
            print(f"Contraseña encontrada: {Password}")
            break