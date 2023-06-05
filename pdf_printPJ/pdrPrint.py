import glob
import PyPDF2 as pd


lst = []
n = int(input("Enter number of pdf sheets"))

for i in range(0, n):
    ele = int(input("Enter you want to print"))
    lst.append(ele)

writer = pd.Pdf.FileWriter()
files = glob.glob('../data/*.pdf')

for i in range(len(files)):
    
