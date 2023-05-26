from PyPDF2 import PdfReader

reader = PdfReader("sample.pdf")

for i in range(len(reader.pages)):
    print("Page:", i)
    print(reader.pages[i].extract_text())
