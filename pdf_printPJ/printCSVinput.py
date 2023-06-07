import glob
import PyPDF2 as pdf
import pandas as pd

csvName = input('Enter csv Name')

d = pd.read_csv('./data/' + csvName, header=None)

writer = pdf.PdfWriter()
files = glob.glob('./data/*.pdf')

for i in range(len(files)):
    reader = pdf.PdfReader(files[i])

    for l in range(0, len(reader.pages)):
        if l in d.values:
            page = reader.pages[l]
            writer.add_page(page)
        
with open("comp.pdf", 'wb') as f:
    writer.write(f)
    
