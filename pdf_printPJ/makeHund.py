import glob
import PyPDF2 as pdf

d = pd.read_csv('./data/test.csv', header=None)

writer = pdf.PdfFileWriter()
files = glob.glob('./data/*.pdf')

for i in range(len(files)):
    reader = pdf.PdfFileReader(files[i])

    for l in range(0, 99):
        if l in d.values:
            page = reader.pages[l]
            writer.addPage(page)
        
with open("comp.pdf", 'wb') as f:
    writer.write(f)
    
