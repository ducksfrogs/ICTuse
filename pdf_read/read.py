import pandas as pd
import fitz

txt_list = []

filename = input('Enter file name :')
doc = fitz.open(filename)

for para in range(len(doc)):
    text = doc[para].get_text()
    text = text.replace('\n', '')
    txt_list.append([para+1, text])


pandaCsv = pd.DataFrame(txt_list)

pandaCsv.to_csv('file/' + filename +'.csv')