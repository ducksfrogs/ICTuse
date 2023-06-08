import glob
import PyPDF2 as pdf
import datetime
import pandas as pd

csvName = input('Enter csv file name: ')

dt = datetime.datetime.now()
fileN = dt.strftime('%Y%m%d_%H%M%S') + 'csvOf.pdf'

d = pd.read_csv('./data/' + csvName, header=None)

writer = pdf.PdfWriter()
files = glob.glob('./data/*.pdf')

for i in range(len(files)):
    reader = pdf.PdfReader(files[i])

    for l in range(0, len(reader.pages)):
        if (l+1) in d.values:
            page = reader.pages[l]
            writer.add_page(page)
        
with open(fileN, 'wb') as f:
    writer.write(f)
    
