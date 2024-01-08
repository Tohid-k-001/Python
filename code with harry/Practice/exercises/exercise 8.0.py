from pypdf import PdfWriter
import os
print(os.getcwd())

merger=PdfWriter()

# by assigning the pdf files as folders and then by givig if condition --

folders=os.listdir("exercises")
print(folders)

for folder in folders:
    if folder.endswith(".pdf"):
        merger.append(folder)

merger.write("merged2-pdf.pdf")
merger.close()