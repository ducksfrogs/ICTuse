import glob
import PyPDF2 as pdfd


lst = []
n = int(input("Enter number of pdf sheets"))

for i in range(0, n):
    ele = int(input("Enter you want to print"))
    lst.append(ele)

writer = pdfd.Pdf.FileWriter()
files = glob.glob('./data/*.pdf')

for i in range(len(files)):
    reader = pdfd.PdfFileReader(files[i])
    for l in range(0, reader.numPages):
        if l in lst:
            page = reader.pages[l]
            writer.addPage(page)

        
with open('comp1.pdf', 'wb') as f:
    writer.write(f)


    

