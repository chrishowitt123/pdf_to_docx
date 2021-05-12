from pdf2docx import Converter
import glob


pdf_files = glob.glob(r'C:\Users\chris\Desktop\States PDFs test\*.pdf')


docx_files = []

for file in pdf_files:
    docx_files.append(file.replace(".pdf", ".docx"))
    

    
    
for pdf, docx in zip(pdf_files, docx_files):
    cv = Converter(pdf)
    cv.convert(docx, start=0, end=None)
    cv.close()
