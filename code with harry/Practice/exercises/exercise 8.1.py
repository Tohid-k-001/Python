from pypdf import PdfWriter
import os

merger=PdfWriter()    #--> created object for PdfWriter

pdffile=[file for file in os.listdir() if file.endswith(".pdf")]  #--> Creted a list of pdf files

for pdf in pdffile:
    merger.append(pdf)     #--> Added each pdf file into merger  

merger.write("merged-pdf.pdf")    #--> named a merged file
merger.close()         #--> Close the object created for PdfWriter
