#################################################################################################
def pdftob64():
    import base64 # importamos la libreria
    pdf = open('HOLAMUNDO.pdf', 'rb') #abrimos  el archivo PDF
    pdf_read = pdf.read() # leemos el archivo
    pdf_64_encode = base64.encodestring(pdf_read) # codificamos el archivo PDF a base64
    #print(pdf_64_encode) #imprimimos
    #image_65_decode = base64.decodestring(image_64_encode)
    #print(image_65_decode)
    return pdf_64_encode
#################################################################################################

def inisializa():
    pdf_64_encode = pdftob64()
    file_name = "HOLAMUNDO.pdf"
    file_type = "application/pdf"
    flag      = bin(3)
    hash      = "SHA1"
    Num_signe = 1

    class requiere:




inisializa()