import glob
import PyPDF2 as pdf

lst = []
n = int(input("Enter number of pdf sheets: "))

for i in range(0, n):
    ele = int(input("Enter you want to print: "))
    lst.append(ele)

writer = pdf.PdfWriter()
files = glob.glob('./data/*.pdf')

for i in range(len(files)):
    reader = pdf.PdfReader(files[i])

    for l in range(0, len(reader.pages)):
        if l in lst:
            page = reader.pages[l]
            writer.add_page(page)
        
with open("comp.pdf", 'wb') as f:
    writer.write(f)
    
